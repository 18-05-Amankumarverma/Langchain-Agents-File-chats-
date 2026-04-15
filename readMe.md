# 📄 PDF Chatbot using LangChain, Pinecone & Groq (LLaMA 3)

This project is a **PDF-based AI chatbot** that allows you to ask questions about a PDF document. It uses **LangChain**, **Pinecone vector database**, **HuggingFace embeddings**, and **Groq LLaMA model** for fast and accurate responses.

---

## 🚀 Features

* 📥 Load and process PDF documents
* ✂️ Smart text chunking
* 🧠 Generate embeddings using HuggingFace
* 🗂️ Store vectors in Pinecone
* 🔍 Retrieve relevant context using similarity search
* 🤖 Answer questions using LLaMA 3 (via Groq API)
* 💬 Interactive chat loop

---

## 🛠️ Tech Stack

* Python
* LangChain
* Pinecone
* HuggingFace Transformers
* Groq API (LLaMA 3)
* dotenv

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory and add:

```env
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_HOST=your_pinecone_host
GROQ_API_KEY=your_groq_api_key
```

---

## 📄 Usage

1. Place your PDF file in the project directory
   Example:

   ```
   facebook.pdf
   ```

2. Run the script:

```bash
python main.py
```

3. Start asking questions:

```
📄 PDF Chat Started (type 'exit' to quit)

👉 You: What is this document about?
🤖 AI: ...
```

---

## ⚙️ How It Works

1. **Load PDF** → Extract text using `PyPDFLoader`
2. **Split Text** → Break into chunks using `RecursiveCharacterTextSplitter`
3. **Embeddings** → Convert text into vectors using HuggingFace model
4. **Store in Pinecone** → Save embeddings for fast retrieval
5. **Retrieve Context** → Find relevant chunks for user query
6. **LLM Response** → Generate answer using LLaMA 3 via Groq

---

## 📁 Project Structure

```
pdf-chatbot/
│── main.py
│── facebook.pdf
│── .env
│── uploaded.flag
│── README.md
```

---

## ⚡ Notes

* The `uploaded.flag` file ensures documents are uploaded **only once** to Pinecone.
* Delete `uploaded.flag` if you want to re-upload updated documents.
* You can replace `facebook.pdf` with any PDF.

---

## 🔧 Customization

* Change embedding model:

```python
model_name="sentence-transformers/all-MiniLM-L6-v2"
```

* Adjust chunk size:

```python
chunk_size=500
chunk_overlap=50
```

* Switch LLM model via Groq:

```python
model="llama-3.3-70b-versatile"
```

---

## ❗ Troubleshooting

* ❌ API errors → Check `.env` keys
* ❌ No results → Ensure PDF is loaded properly
* ❌ Pinecone issues → Verify index host and API key

---

## 📌 Future Improvements

* Web UI (Streamlit / React)
* Multi-PDF support
* Chat history memory
* Authentication system
* Upload PDFs dynamically

---

## 👨‍💻 Author

Aman Kumar Verma

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
