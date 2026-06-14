# 🌴 Chatbot Pemeliharaan Sawit AI
🌴 Chatbot Pemeliharaan Sawit AI

Chatbot AI berbasis:

Google Gemini 2.5 Flash
LangChain
ChromaDB
Streamlit
RAG (Retrieval-Augmented Generation)
Fitur
Tanya jawab seputar pemeliharaan kelapa sawit
Membaca dokumen PDF
Pencarian informasi berbasis RAG
Antarmuka web menggunakan Streamlit
Instalasi

Clone repository:

git clone https://github.com/username/sawit-chatbot-rag.git
cd sawit-chatbot-rag

Install dependency:

pip install -r requirements.txt
Environment Variables

Salin file .env.example menjadi .env

cp .env.example .env

Isi file .env:

GOOGLE_API_KEY=API_KEY_ANDA
NGROK_AUTH_TOKEN=TOKEN_NGROK_ANDA
Menjalankan Aplikasi
streamlit run app.py
Struktur Proyek
sawit-chatbot-rag/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
└── panduan_sawit.pdf
Lisensi

MIT License
(Tempel isi README di atas di sini)
