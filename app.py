# app.py
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA

# ----------------------------
# Step 1: Extract text from PDF
# ----------------------------
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

# ----------------------------
# Step 2: Chunk the text
# ----------------------------
def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(text)

# ----------------------------
# Step 3: Embed chunks with FAISS
# ----------------------------
def create_faiss_index(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_texts(chunks, embeddings)
    return db

# ----------------------------
# Step 4: Set up QA chain using LlamaCpp
# ----------------------------
def create_qa_chain(db):
    llm = LlamaCpp(
        model_path="./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",  # Path to your GGUF model
        n_ctx=4096,
        temperature=0.7,
        top_p=0.9,
        n_gpu_layers=32,
        verbose=True,
    )
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    return qa

# ----------------------------
# Main CLI loop
# ----------------------------
def main():
    print("🔍 PDF Chat Assistant with Mistral 7B")
    pdf_path = input("📄 Enter the path to your PDF file (e.g., docs/sample.pdf): ").strip()

    if not os.path.exists(pdf_path):
        print("❌ PDF file not found!")
        return

    print("⏳ Extracting text...")
    raw_text = extract_text_from_pdf(pdf_path)

    print("✂️ Splitting into chunks...")
    chunks = chunk_text(raw_text)

    print("🧠 Creating vector index...")
    db = create_faiss_index(chunks)

    print("🤖 Loading Mistral 7B and setting up QA system...")
    qa_chain = create_qa_chain(db)

    print("\n✅ Ready! Ask questions about your PDF. Type 'exit' to quit.\n")
    while True:
        query = input("❓ You: ")
        if query.lower() in ("exit", "quit"):
            break
        response = qa_chain.invoke({"query": query})
        print("💬 Answer:", response, "\n")

if __name__ == "__main__":
    main()
