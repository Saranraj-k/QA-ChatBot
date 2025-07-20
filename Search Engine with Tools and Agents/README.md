

# 🔍 LangChain Search Agent with Tools (Wikipedia, Arxiv, DuckDuckGo)

This project is an intelligent search engine chatbot built using [LangChain](https://www.langchain.com/), [Streamlit](https://streamlit.io/), and [Groq LLMs](https://groq.com/). The chatbot utilizes multiple tools (Wikipedia, Arxiv, and DuckDuckGo Search) to answer queries intelligently using an agent-based approach.

<img width="1905" height="786" alt="image" src="https://github.com/user-attachments/assets/70d1034b-2581-45f3-95a1-ed2aea687a40" />


---

## 🚀 Features

- ✅ Uses Groq LLM (like `gemma2-9b-it`) for intelligent responses
- ✅ LangChain Agent with tool calling support
- ✅ Accesses real-time info from:
  - Wikipedia
  - Arxiv
  - DuckDuckGo
- ✅ Streamlit-powered interactive chat interface
- ✅ Callback handler for tool usage tracing (optional)

---

## 🛠️ Tech Stack

- **LangChain**
- **Groq LLMs** via `langchain_groq`
- **Streamlit** UI
- **DuckDuckGo**, **Wikipedia**, **Arxiv** integrations via LangChain community tools
- **dotenv** for API key management

---

## 📦 Installation

```bash
git clone https://github.com/your-username/langchain-search-agent.git
cd langchain-search-agent
pip install -r requirements.txt
````

---

## 🔐 Setup

1. Create a `.env` file in the root directory with your Groq and HuggingFace API keys:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingfacehub_token
```

> ⚠️ You’ll be prompted for your Groq API key in the Streamlit sidebar at runtime.

---

## 🧠 How It Works

* Loads 3 tools: **Wikipedia**, **Arxiv**, and **DuckDuckGo**
* Initializes a **LangChain Agent** using `ZERO_SHOT_REACT_DESCRIPTION`
* Accepts a natural language query via **Streamlit chat input**
* Routes query to the most appropriate tool
* Uses **Groq LLM** to generate and return a final answer

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open your browser to the local Streamlit URL (usually [http://localhost:8501](http://localhost:8501)).

---

## 💡 Example Prompts

* “What is Quantum Computing?”
* “Recent papers on diffusion models from Arxiv”
* “Who is the current CEO of Google?”

---

## 📁 Project Structure

```
.
├── app.py               # Main Streamlit app
├── .env                 # Your environment file (not committed)
├── requirements.txt     # Dependencies
└── README.md            # This file

```
