# 📚 LangChain Summarizer: YouTube & Website Content

This is a Streamlit-based web application that summarizes content from YouTube videos or web pages using the [LangChain](https://www.langchain.com/) framework with the [Groq API](https://groq.com/).
<img width="1735" height="827" alt="image" src="https://github.com/user-attachments/assets/ea3d302a-dca4-451c-a16e-74e44c544995" />

## 🚀 Features

- 🔗 Accepts any YouTube or Website URL.
- 🤖 Uses `ChatGroq` LLM (`gemma2-9b-it`) to generate concise summaries.
- 🧠 Supports map-reduce summarization for efficient and effective content summarization.
- 🛠️ Automatically detects if a link is a YouTube video or a web page.
- 🧱 Built using:
  - `Streamlit` for UI
  - `LangChain` for chaining LLMs
  - `Groq API` for fast LLM inference
  - `YoutubeLoader` and `UnstructuredURLLoader` from `langchain_community` for loading content

---

## 📦 Installation

```bash
# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

### ✍️ `requirements.txt`

```txt
streamlit
langchain
langchain-groq
langchain-community
validators
```

---

## 🧪 Usage

1. **Run the app**:

```bash
streamlit run app.py
```

2. **Enter your [Groq API Key](https://console.groq.com/) in the sidebar**.
3. **Paste a YouTube or Website URL**.
4. Click on **"Summarize the content from YT or Website"**.
5. 🎉 Enjoy a clean and concise summary!

---

## 📂 Project Structure

```
.
├── app.py                 # Main Streamlit app
├── README.md              # This file
├── requirements.txt       # Python dependencies
```

---

## ⚠️ Notes

* If you're using a **YouTube link**, ensure it has transcripts available.
* Website summarization might not work on pages that block bots or require authentication.

---

## 🧠 Example Use Cases

* Quickly understand long-form content from podcasts or interviews.
* Summarize research articles or news articles.
* Generate short briefs from any public URL.

---

## 🙏 Acknowledgements

* [LangChain](https://www.langchain.com/)
* [Groq](https://groq.com/)
* [Streamlit](https://streamlit.io/)
* [LangChain Community Loaders](https://docs.langchain.com/docs/modules/data_connection/document_loaders/)
