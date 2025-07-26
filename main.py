import gradio as gr
from langchain_community.llms import Ollama
from vector_store import create_vector_store

retriever = None
llm = Ollama(model="llama3.2")

def upload_and_load(file_path):
    global retriever
    if file_path is None:
        return "Please upload a file."
    try:
        retriever = create_vector_store(file_path)
        return "File uploaded and indexed successfully."
    except Exception as e:
        return f"Error: {e}"

def ask_question(query):
    global retriever, llm
    if retriever is None:
        return "Please upload and index a file first."
    try:
        docs = retriever.get_relevant_docs(query, top_k=3)
        context = "\n\n".join([d.page_content for d in docs])
        prompt = f"Answer the question based on the following context:\n{context}\n\nQuestion: {query}\nAnswer:"
        return llm(prompt)
    except Exception as e:
        return f"Error: {e}"

with gr.Blocks(title="RAG Chatbot with LLaMA 3.2") as demo:
    gr.Markdown("## Ask Questions Based on Your Document (RAG with LLaMA 3.2)")

    with gr.Row():
        file_upload = gr.File(label="Upload Document", file_types=[".pdf", ".docx", ".txt", ".csv", ".xlsx"], type="filepath")
        upload_btn = gr.Button("Process File")

    status = gr.Textbox(label="Status", interactive=False)
    user_input = gr.Textbox(label="Ask a Question")
    answer = gr.Textbox(label="Answer", lines=5)

    upload_btn.click(upload_and_load, inputs=file_upload, outputs=status)
    user_input.submit(ask_question, inputs=user_input, outputs=answer)

if __name__ == "__main__":
    demo.launch()
