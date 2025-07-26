# Rag-ChatBot
RAG Chatbot using Ollama  This project implements a Retrieval-Augmented Generation (RAG) chatbot that uses Ollama with LLaMA 3.2 to answer user questions based on uploaded documents (PDF, DOCX, TXT, CSV, XLSX). It combines LangChain, FAISS, and Gradio to enable local, private document-based Q&amp;A with fallback handling for unrelated queries.

# RAG Chatbot using Ollama

This project implements a fully functional Retrieval-Augmented Generation (RAG) chatbot that leverages LLaMA 3.2 via Ollama, integrated with LangChain, FAISS, and Gradio. The chatbot is capable of answering user queries based on uploaded document content (PDF, DOCX, TXT, CSV, XLSX). If a query is unrelated to the provided documents, the chatbot responds appropriately with a fallback message.

## Project Overview

The RAG architecture enhances LLM performance by grounding responses in domain-specific data provided at runtime. This chatbot reads documents, embeds them using FAISS, and retrieves the most relevant chunks to inform the LLM’s response. It supports multiple file formats and operates locally, making it suitable for private or offline use cases.

## Features

- Retrieval-augmented QA with context-aware responses
- Multi-format document ingestion (PDF, DOCX, TXT, CSV, XLSX)
- Fallback response for queries outside the document context
- Lightweight GUI powered by Gradio
- Fully local execution using Ollama + LLaMA 3.2

## Technology Stack

- **Programming Language**: Python
- **LLM Interface**: Ollama with LLaMA 3.2
- **Retrieval Engine**: FAISS (Vector Similarity Search)
- **Frameworks**: LangChain, Gradio
- **Data Preprocessing**: PyPDF2, pdfplumber, python-docx, pandas, openpyxl, unstructured

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/rag-chatbot-ollama.git
   cd rag-chatbot-ollama
   
2. Create and Activate Virtual Environment
   python3 -m venv venv
   source venv/bin/activate
   
3.Ensure Ollama is Running with LLaMA 3.2
  ollama pull llama3
  ollama run llama3

4.Start the Chatbot
  python main.py



