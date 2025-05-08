# 🧠 AskMyPDF

AskMyPDF is an AI-powered web app that allows users to upload a PDF and ask natural language questions about its content. It's a helpful tool for understanding research papers, extracting key insights from long documents, or interacting with contracts and manuals — all without reading the whole file.

---

## 🚀 Features

- 📄 Upload a PDF file
- 💬 Ask any question related to the document
- 🤖 Get instant, accurate AI responses
- 🧠 Uses vector search and a large language model (LLM) to understand context
- ⚙️ Built with modular, scalable components

---

## 🛠️ Tech Stack

| Layer       | Technology                     |
|------------|---------------------------------|
| Frontend    | Streamlit (for quick UI)        |
| Backend     | Python                          |
| AI Model    | OpenAI GPT / DeepSeek / Local LLM (via Ollama) |
| Embeddings  | OpenAI / HuggingFace Embeddings |
| Vector DB   | FAISS / ChromaDB                |
| PDF Parsing | PyPDF2 / PDFMiner / PDFplumber  |
| Deployment  | Streamlit Cloud / Localhost     |

---

## 🧠 How It Works

1. **PDF Upload**: User uploads a PDF through the web interface.
2. **Text Extraction**: The app extracts and splits the PDF into chunks.
3. **Embeddings**: Each chunk is converted into vector embeddings.
4. **Vector Search**: When a question is asked, the app searches for the most relevant chunks.
5. **LLM Query**: Relevant chunks + question are passed to an LLM to generate a precise, contextual answer.

---

## 💻 Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/askmypdf.git
cd askmypdf
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file in the root directory and add:

```ini
OPENAI_API_KEY=your_openai_key_here
```

*(Or set up Ollama or another provider depending on your model choice.)*

### 5. Run the App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📸 Screenshots

*coming soon*

---

## 📌 Future Improvements

- PDF preview and highlighting for answers  
- Chat history and session download  
- Summarization and key points extraction  
- User login & cloud PDF storage  

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Credits

Built with ❤️ using **Streamlit**, **LangChain**, **FAISS**, and **OpenAI**.
