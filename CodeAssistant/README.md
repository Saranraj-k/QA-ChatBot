
# 🧑‍💻 Coder: Code Teaching Assistant (Gradio + Ollama + CodeLlama)

This is a simple yet powerful **code teaching assistant chatbot**, named **Coder**, built using [Gradio](https://www.gradio.app/) for the UI and [Ollama](https://ollama.com/) for local LLM inference. The model used here is `codeguru` (a variant of CodeLlama or any code-supporting model).

---

## 🚀 Features

- ✅ Interactive code question & answer chat UI using Gradio
- ✅ Uses Ollama API to run CodeLlama (or other models) locally
- ✅ Maintains conversation history for better context
- ✅ Easy to customize with temperature, system prompt, etc.

---

## 🛠️ Requirements

- Python 3.8+
- `gradio`
- `requests`
- `ollama` running locally with the model pulled

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/code-assistant-ollama.git
cd code-assistant-ollama
pip install -r requirements.txt
````

Make sure you have [Ollama](https://ollama.com/download) installed and running locally. Start the model using:

```bash
ollama run codeguru
```

You can change the model to `codellama` or any other LLM.

---

## 🧠 System Prompt & Model

The assistant is initialized with the following system prompt:

```
You are a code teaching assistant named as Coder created by
Saran. Answer all the code-related questions being asked.
```

You can update this in the Ollama `Modelfile` if you're fine-tuning or want to change behavior.

---

## 💻 How to Run

```bash
python app.py
```

Then, go to `http://localhost:7860` in your browser to chat with **Coder**!

---

## 📝 Sample Modelfile for Ollama

You can create a custom `Modelfile` to fine-tune the behavior:

```
FROM codellama

PARAMETER temperature 1

SYSTEM """
You are a code teaching assistant named as coder created by
Saran. Answer all the code related questions being asked.
"""
```

Build with:

```bash
ollama create codeguru -f Modelfile
```

---
## ✨ Credits


* [Gradio](https://gradio.app)
* [Ollama](https://ollama.com)
* [CodeLlama](https://ai.meta.com/llama)

