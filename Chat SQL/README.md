# 🧠 Chat with SQL Database using LangChain + Groq + Streamlit

This project is an intelligent chatbot interface built with **Streamlit**, powered by **LangChain** and **Groq LLMs**, that allows users to interact with a **SQLite** or **MySQL** database using natural language.

> Ask questions like:
> - "How many students scored more than 90?"
> - "Show the top 5 students by marks"
> - "What is the average age of students?"

---

<img width="1920" height="860" alt="image" src="https://github.com/user-attachments/assets/32cf9d17-0327-478f-af56-09c2f2def1ce" />

---

## 🚀 Features

- 🔗 **Connect to SQLite or MySQL database**
- 🤖 **Chat with your DB using Groq LLM (`gemma2-9b-it`)**
- 🛠️ Built with LangChain's **SQLDatabaseToolkit + Agents**
- 💬 Simple Streamlit-based chat UI
- 🔐 Secure credential input via sidebar

---

## 🧱 Tech Stack

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Groq LLMs](https://groq.com/)
- SQLAlchemy + SQLite3 / MySQL
- dotenv (optional) for environment management

---

## 📦 Installation

```bash
git clone https://github.com/your-username/langchain-sql-chatbot.git
cd langchain-sql-chatbot
pip install -r requirements.txt
````

---

## 🔐 Environment Setup

Create a `.env` file in the root directory if you want to store API keys:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingfacehub_token  # optional if using huggingface
```

---

## 🧠 How It Works

1. Choose between:

   * ✅ Preloaded SQLite3 `student.db`
   * ✅ Your own MySQL DB connection
2. Enter your **Groq API key**
3. Type your natural language question in the chat
4. The LangChain Agent:

   * Analyzes your question
   * Uses SQL toolkit to query the DB
   * Responds using LLM output

---

## ▶️ Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📝 Usage Notes

* For SQLite, ensure `student.db` is present in the same directory as `app.py`.
* For MySQL:

  * Provide `host`, `username`, `password`, and `database name` in the sidebar
  * The app will connect using SQLAlchemy

---

## 💬 Example Prompts

* "List all students in class 10"
* "Who is the oldest student?"
* "Average marks by subject"

---

## 📁 File Structure

```
.
├── app.py               # Main Streamlit application
├── student.db           # Sample SQLite3 DB (optional)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 🔧 Requirements

Add this to your `requirements.txt`:

```txt
streamlit
langchain
langchain_groq
langchain-community
sqlalchemy
sqlite3
mysql-connector-python
python-dotenv

