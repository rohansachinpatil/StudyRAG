# StudyRAG ⚡ — AI Study Assistant

StudyRAG is a professional, AI-powered study assistant inspired by Google's NotebookLM. It allows students and researchers to upload their learning materials (PDFs, textbooks, lecture notes) and interact with them through a sophisticated Retrieval-Augmented Generation (RAG) pipeline.

![StudyRAG UI](https://img.icons8.com/color/96/artificial-intelligence.png)

## 💡 The Problem
In today's digital age, students are overwhelmed with information. Traditional search is keyword-based and often fails to find deep insights buried in 500-page textbooks or complex lecture notes. **StudyRAG** solves this by providing a semantic interface to your documents—allowing you to have a natural conversation with your data.

## ✨ Key Features
- **NotebookLM-Style UI**: A clean, light-themed interface designed for focus, utilizing Lucide Icons and modern typography.
- **Semantic Retrieval**: Uses MMR (Maximal Marginal Relevance) to find the most diverse and relevant context from your documents.
- **Mistral Powered**: Utilizes Mistral Small (`mistral-small-2506`) for high-quality, grounded academic answers.
- **Citations**: Automatically highlights the source text used to generate each answer, ensuring academic integrity.
- **Cross-Platform**: Fully responsive design for Mobile, Tablet, and Desktop.

## 🚀 How It Works
StudyRAG transforms raw text into a searchable knowledge base:
1. **Ingestion**: PDFs and TXT files are processed and split into optimized chunks.
2. **Vectorization**: Text is converted into high-dimensional vectors using **Mistral API Embeddings**.
3. **Storage**: Data is stored in **ChromaDB**, allowing for lightning-fast semantic lookups.
4. **Generation**: When you ask a question, the system retrieves relevant chunks and uses an LLM to generate a factual, grounded response.

## 🛠️ Tech Stack
- **Backend**: FastAPI (Python)
- **RAG Framework**: LangChain
- **LLM & Embeddings**: Mistral AI
- **Vector Store**: ChromaDB
- **Frontend**: Vanilla JS, HTML5, CSS3, Lucide Icons

## 🤝 Contributing & PRs
We welcome contributions! Whether it's adding support for more file formats, improving the UI, or optimizing the retrieval logic, feel free to open an issue or submit a Pull Request.

**Pull Requests are accepted and encouraged!**

---
*Designed & Developed by [Rohan Patil](https://github.com/rohansachinpatil)*
