# ai-model
# 🦙 Local PDF Chat Assistant using LLaMA

A lightweight local application to **chat with PDF files** using a locally hosted LLaMA-based model. Upload a PDF, ask questions, and get contextual answers — all without sending data to external servers.

## 🔧 Features

- Upload and parse PDF documents.
- Ask natural language questions about the PDF.
- Get answers from a locally running LLaMA model (no internet needed).
- Simple Flask-based web interface.

---

## 📁 Project Structure

```
.
├── app.py              # Main Flask server
├── llama_local.py      # LLaMA model loader and response generator
├── pdf_loader.py       # PDF text extractor
├── requirements.txt    # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pdf-llama-assistant.git
cd pdf-llama-assistant
```

### 2. Install dependencies

We recommend using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Add your LLaMA model

Make sure you have a local GGUF version of a LLaMA model placed in the appropriate path (used in `llama_local.py`). Example path:
```
models/llama-2-7b-chat.gguf
```

You can change the model path in `llama_local.py`.

### 4. Run the application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 📷 Screenshots

*(Add screenshots of your app here if available.)*

---

## 🧠 How it Works

- The PDF is uploaded via the web interface.
- `pdf_loader.py` extracts the full text content from the PDF.
- User questions are passed to the local LLaMA model via `llama_local.py`.
- The LLaMA model generates a response based on the combined context and user query.

---

## ✅ Requirements

- Python 3.8+
- Sufficient RAM and GPU (or CPU support) to load LLaMA model
- PDF documents in English (best results with well-structured PDFs)

---

## 📌 Notes

- All processing is done **locally** — your data never leaves your device.
- You can swap in other GGUF-compatible models by updating `llama_local.py`.

---

## 🛠 Future Improvements

- Multi-PDF support
- Chat history
- Better PDF section referencing
- UI improvements (streamlit or React frontend)

---

## 📃 License

MIT License. See `LICENSE` file (add this if needed).
