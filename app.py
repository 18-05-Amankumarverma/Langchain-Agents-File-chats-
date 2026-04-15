import os
from dotenv import load_dotenv
from pinecone import Pinecone

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI

# ------------------ LOAD ENV ------------------
load_dotenv()

# ------------------ INIT PINECONE ------------------
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(host=os.getenv("PINECONE_HOST"))

# ------------------ LOAD PDF ------------------
loader = PyPDFLoader("facebook.pdf")
documents = loader.load()

# ------------------ SPLIT ------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# ------------------ EMBEDDINGS ------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ------------------ VECTOR STORE ------------------
vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

# Store only once (optional: you can comment after first run)
if not os.path.exists("uploaded.flag"):
    vectorstore.add_documents(docs)
    open("uploaded.flag", "w").close()

# ------------------ RETRIEVER ------------------
retriever = vectorstore.as_retriever()

# ------------------ LLM ------------------
llm = ChatOpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    model="llama-3.3-70b-versatile"
)

# ------------------ CHAT LOOP ------------------
print("\n📄 PDF Chat Started (type 'exit' to quit)\n")

while True:
    query = input("👉 You: ")

    if query.lower() in ["exit", "quit"]:
        print("👋 Exiting...")
        break

    # Retrieve relevant docs
    retrieved_docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    # Generate response
    response = llm.invoke(
        f"Answer based on this context:\n{context}\n\nQuestion: {query}"
    )

    print("\n🤖 AI:", response.content, "\n")