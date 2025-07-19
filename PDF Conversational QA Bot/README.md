# 📄 PDF Conversational QA Bot 🤖

A powerful and interactive Streamlit-based chatbot that lets you upload and chat with PDF documents using advanced Retrieval-Augmented Generation (RAG) with LangChain, Chroma vector DB, and Groq's Gemma-2 LLM.

---

<img width="1144" height="548" alt="image" src="https://github.com/user-attachments/assets/14555775-9919-4e2f-9bc3-632ca3148272" />


## 🚀 Features

- 📁 Upload one or multiple PDF files
- 🔍 Automatically chunk and embed content using HuggingFace embeddings
- 💬 Ask contextual questions — the bot understands chat history!
- 🧠 Uses LangChain RAG architecture
- 📦 Embeds stored in Chroma vector DB
- 🧵 Maintains chat history across sessions
- 🔐 Secure API integration with Groq’s Gemma-2 LLM

---

## 🖥️ Demo

> ![App Screenshot](https://user-images.githubusercontent.com/your-username/pdf-bot-demo.png)

---

## 🛠️ Tech Stack

- **[LangChain](https://www.langchain.com/)** – Framework for building LLM-powered applications
- **[Streamlit](https://streamlit.io/)** – Interactive UI
- **[Chroma](https://www.trychroma.com/)** – Vector database
- **[Groq](https://groq.com/)** – Ultra-fast inference for Gemma-2 model
- **[HuggingFace Embeddings](https://huggingface.co/)** – For document vectorization
- **PDF Loader** – Extracts content from PDF files
- **RAG + History Aware Retriever** – Improves context understanding in conversations

---

## 🔧 Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/pdf-qa-bot.git
cd pdf-qa-bot
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # on Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables

Create a `.env` file in the root directory and add your HuggingFace API key:

```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

You will enter your **Groq API key** inside the Streamlit app when prompted.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 Usage

1. Start the app.
2. Enter your **Groq API Key**.
3. Enter a **Session ID** (for chat history).
4. Upload one or more **PDF files**.
5. Ask any question related to the uploaded PDF content!

---

## 📁 Project Structure

```
pdf-qa-bot/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Required Python packages
├── .env                   # HuggingFace API key (not committed)
└── README.md              # Project documentation
```

---

## 🧠 Behind the Scenes

* **Text Splitter**: Splits large PDF text into manageable chunks.
* **Embeddings**: Converts text chunks to vector representations.
* **VectorStore (Chroma)**: Stores vectors for fast similarity search.
* **LangChain Retriever**: Uses previous chat history to understand context better.
* **LLM (Groq + Gemma2)**: Answers your question concisely and contextually.

---

## ⚠️ Troubleshooting

* **Chroma `default_tenant` Error**:
  Add `persist_directory="./chroma_db"` while initializing the Chroma vectorstore.

* **No Answer / Irrelevant Answer**:
  Ensure the PDF is well-formatted and questions are clearly framed.

---

## 💡 Inspiration

This project is inspired by the need to make large documents conversational and easily queryable using cutting-edge GenAI tools.

