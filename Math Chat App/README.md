# 📐 Math Problem Solver App

An interactive Streamlit application powered by [LangChain](https://www.langchain.com/) and [Groq's Gemma2-9B-IT model](https://groq.com/) that can **solve complex math problems**, **reason through them step-by-step**, and optionally use **Wikipedia** for additional context!

> 🚀 Built with `LangChain`, `Streamlit`, and the blazing fast `Groq` API.

---
<img width="1917" height="846" alt="image" src="https://github.com/user-attachments/assets/3c320aca-599b-4f94-880c-643a742ec87a" />

## 🧠 Features

- ✍️ Accepts **natural language math questions**
- 🧮 Uses a **calculator chain** for mathematical computation
- 🤖 Uses an **LLMChain for logical step-by-step reasoning**
- 📚 Fetches **relevant information from Wikipedia**
- 💬 Chat-style interface with message history
- 🧑‍🏫 Final output is clear, structured, and beginner-friendly

---

## 📸 Demo Screenshot

![Math Solver Screenshot](assets/screenshot.png)

---

## 🔧 Requirements

- Python 3.8+
- Groq API Key (free signup at [Groq Cloud](https://console.groq.com/))

---

## 🚀 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/math-problem-solver.git
cd math-problem-solver
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run app.py
```

---

## 🔑 Add Your Groq API Key

The app requires a valid Groq API key. Enter it in the **sidebar** when prompted.

You can get your API key by signing up at [https://console.groq.com](https://console.groq.com)

---

## 📁 Project Structure

```
math-problem-solver/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
└── assets/
    └── screenshot.png    # Optional screenshot for README
```

---

## 💡 How It Works

The app combines multiple LangChain tools into a single agent:

* `Calculator`: For numerical problems
* `Wikipedia`: For knowledge questions
* `Reasoning`: Custom prompt to explain solutions step-by-step

It uses **LangChain’s `initialize_agent()`** with the `ZERO_SHOT_REACT_DESCRIPTION` agent type to decide which tool to use based on your query.

---

## 📚 Example Questions

* *How much time will 5 workers take to complete 1/3rd of a task if 3 workers can finish it in 9 hours?*
* *Tell me how 4 cranes can be used to lift 1000 kg in 10 minutes*
* *What is the area of a circle with radius 6?*
* *Explain how compound interest is calculated for 3 years with 5% rate.*

---

## ✨ Acknowledgements

* [LangChain](https://www.langchain.com/)
* [Streamlit](https://streamlit.io/)
* [Groq API](https://groq.com/)
* [Wikipedia LangChain Wrapper](https://docs.langchain.com/docs/integrations/tools/wikipedia)

