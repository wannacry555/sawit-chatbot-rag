
import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings

# =====================
# LOAD PDF
# =====================

loader = PyPDFLoader("panduan_sawit.pdf")
docs = loader.load()

# =====================
# SPLIT
# =====================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

documents = splitter.split_documents(docs)

# =====================
# EMBEDDING
# =====================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =====================
# VECTOR DB
# =====================

db = Chroma.from_documents(
    documents,
    embeddings
)

retriever = db.as_retriever(
    search_kwargs={"k":3}
)

# =====================
# GEMINI
# =====================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2
)

# =====================
# STREAMLIT UI
# =====================

st.set_page_config(
    page_title="Chatbot Sawit"
)

st.title("🌴 Chatbot Pemeliharaan Sawit")

question = st.chat_input(
    "Tanyakan sesuatu tentang sawit..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [d.page_content for d in docs]
    )

    prompt = f"""
    Anda adalah ahli kelapa sawit.

    Jawablah hanya berdasarkan konteks berikut.

    KONTEKS:
    {context}

    PERTANYAAN:
    {question}
    """

    response = llm.invoke(prompt)

    with st.chat_message("assistant"):
        st.write(response.content)
