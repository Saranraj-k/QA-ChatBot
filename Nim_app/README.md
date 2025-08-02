# 🤖 Nvidia NIM RAG Chatbot with Streamlit

Welcome to the **Nvidia NIM RAG Chatbot**! This project leverages the power of Nvidia's LLMs and FAISS vector search to provide accurate answers to your questions from PDF documents. The app is built using [Streamlit](https://streamlit.io/) for a simple and interactive user experience.

---

## 📚 Features

- **PDF Document Loader**: Easily loads and parses PDF files.
- **Text Chunking**: Splits documents into manageable chunks for better retrieval.
- **FAISS Vector Store**: Efficient vector similarity search for finding relevant document sections.
- **Nvidia LLM Integration**: Uses Nvidia's `meta/llama3-70b-instruct` for high-quality answers.
- **Interactive UI**: Ask questions and view source document excerpts in a friendly web app.
- **.env Support**: Securely manage your Nvidia API key.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/nvidia-nim-rag-chatbot.git
cd nvidia-nim-rag-chatbot
```

### 2. Install Dependencies

It's recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file in the project root:

```
NVIDIA_API_KEY=your_nvidia_api_key_here
```

### 4. Add Your PDF

Place your PDF file (e.g., `Speech - Wikipedia.pdf`) in the project directory.

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🛠️ Configuration

- **PDF File**: By default, the app loads `Speech - Wikipedia.pdf`. Change this in `app.py` as needed.
- **Model**: Uses `meta/llama3-70b-instruct` via Nvidia API.

---

## 💡 How to Use

1. Click **Documents Embedding** to load and index your PDF.
2. Type your question in the text box.
3. Get instant, context-aware answers! 🎉
4. Expand **Document Similarity search** to view relevant source document snippets.

---

## 📦 Dependencies

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [langchain-nvidia-ai-endpoints](https://github.com/langchain-ai/langchain-nvidia-ai-endpoints)
- [FAISS](https://github.com/facebookresearch/faiss)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

**Happy chatting! 🤗🤖**
