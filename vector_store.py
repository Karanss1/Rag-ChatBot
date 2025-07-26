import os
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class TfidfRetriever:
    def __init__(self, docs):
        self.docs = docs
        self.texts = [doc.page_content for doc in docs]
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.doc_vectors = self.vectorizer.fit_transform(self.texts)

    def get_relevant_docs(self, query, top_k=3):
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.doc_vectors).flatten()
        top_indices = np.argsort(scores)[::-1][:top_k]
        return [self.docs[i] for i in top_indices]

def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == ".pdf":
            import pdfplumber
            with pdfplumber.open(file_path) as pdf:
                return "\n".join(page.extract_text() or "" for page in pdf.pages)
        elif ext == ".docx":
            from docx import Document as DocxDocument
            doc = DocxDocument(file_path)
            return "\n".join(p.text for p in doc.paragraphs)
        elif ext == ".csv":
            import pandas as pd
            return pd.read_csv(file_path).to_string()
        elif ext == ".xlsx":
            import pandas as pd
            return pd.read_excel(file_path).to_string()
        elif ext == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        else:
            # fallback
            return ""
    except Exception as e:
        return f"Error reading file: {e}"

def create_vector_store(file_path):
    text = read_file(file_path)
    if not text or text.startswith("Error"):
        raise ValueError("No text extracted from document or error reading file.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text], metadatas=[{"source": os.path.basename(file_path)}])

    retriever = TfidfRetriever(docs)
    return retriever
