from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import tempfile

from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use Mistral Embeddings for Vercel (API-based, no local model download)
embedding_model = MistralAIEmbeddings()

# Note: In Vercel, this vectorstore will be recreated on every cold start.
# For permanent storage, you would connect to a cloud DB like Pinecone or MongoDB Atlas.
vectorstore = Chroma(
    embedding_function=embedding_model
)

llm = ChatMistralAI(model="mistral-small-2506")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI study assistant.
Use ONLY the provided context to answer the question.
If the answer is not present in the context, say: "I could not find the answer in the document."
Be clear, concise, and helpful."""),
    ("human", "Context:\n{context}\n\nQuestion:\n{question}")
])

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Look for index.html in the root or static folder
    path = "index.html"
    if not os.path.exists(path):
        path = os.path.join("static", "index.html")
    
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    if file.filename.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path, encoding="utf-8")
        
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    vectorstore.add_documents(chunks)
    return {"message": f"Successfully uploaded {file.filename}", "chunks_count": len(chunks)}

class ChatRequest(BaseModel):
    query: str

@app.post("/chat")
async def chat(request: ChatRequest):
    query = request.query
    retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 4})
    retrieved_docs = retriever.invoke(query)
    
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    final_prompt = prompt_template.invoke({"context": context, "question": query})
    response = llm.invoke(final_prompt)
    
    retrieved_chunks = [{"chunk": doc.page_content, "score": 1.0} for doc in retrieved_docs]

    return {
        "answer": response.content,
        "retrieved": retrieved_chunks
    }
