# StudyRAG ⚡ — AI Study Assistant

StudyRAG is a professional, AI-powered study assistant inspired by Google's NotebookLM. It allows students to upload their learning materials (PDFs, textbooks, lecture notes) and interact with them using a Retrieval-Augmented Generation (RAG) pipeline.

![StudyRAG UI](https://img.icons8.com/color/96/artificial-intelligence.png)

## 💡 The Problem
In today's digital age, students are overwhelmed with information. Traditional search is keyword-based and often fails to find deep insights buried in 500-page textbooks or complex lecture notes. **StudyRAG** solves this by providing a semantic interface to your documents—allowing you to have a natural conversation with your data.

## ✨ Key Features
- **Modern UI**: Clean, light-themed interface inspired by Google's NotebookLM, using **Lucide Icons** for a professional look.
- **Custom Branding**: Features a stylized AI brain logo in the navigation.
- **Multi-Format Support**: Upload PDFs and TXT files directly through a drag-and-drop zone.
- **Smart Retrieval**: Uses MMR (Maximal Marginal Relevance) to find the most diverse and relevant context from your documents.
- **Mistral Powered**: Utilizes Mistral Small for high-quality, lightning-fast academic answers.
- **Citations**: Automatically highlights the source text used to generate each answer with dedicated citation cards.

## 🚀 How It Works (The RAG Pipeline)
1. **Upload**: User uploads PDFs, lecture notes, or textbooks.
2. **Loading**: System converts raw files into processable Document objects.
3. **Chunking**: Documents are split into 1000-character chunks with a 200-character overlap for accuracy.
4. **Embedding**: Chunks are transformed into numerical vectors using **Mistral Embeddings**.
5. **Storage**: Vectors and original text are stored in a **ChromaDB** vector database.
6. **Querying**: User asks a question, which is converted into an embedding.
7. **Similarity Search**: The system performs a semantic search to find relevant document chunks.
8. **MMR Retrieval**: The top-k chunks are selected to provide context.
9. **LLM Generation**: The Mistral LLM generates a grounded answer based *only* on the provided context.
10. **Delivery**: The student receives a precise answer with source citations.

## 🛠️ Tech Stack
- **Backend**: FastAPI (Python)
- **Framework**: LangChain
- **LLM**: Mistral AI (`mistral-small-2506`)
- **Embeddings**: Mistral AI Embeddings
- **Vector Store**: ChromaDB
- **Frontend**: Vanilla JS, HTML5, CSS3
- **Icons**: Lucide Icons

## 💻 Local Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd RAGproject
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file and add your Mistral API key:
   ```env
   MISTRAL_API_KEY=your_key_here
   ```

5. **Run the app**:
   ```bash
   python -m uvicorn api.index:app --reload
   ```
   Visit `http://127.0.0.1:8000`

## ☁️ Deployment (Vercel)
This project is pre-configured for Vercel Serverless Functions.

1. Connect your repository to **Vercel**.
2. Add your `MISTRAL_API_KEY` to the **Environment Variables** in the Vercel Dashboard.
3. Deploy!

---
*Designed & Developed by [Rohan Patil](https://github.com/rohansachinpatil)*
