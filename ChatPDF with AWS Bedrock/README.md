# 🦙📄 Chat with PDFs using Amazon Bedrock & LangChain

This application allows users to **chat with PDF documents** using Amazon Bedrock's foundation models like **Claude** and **LLaMA2**, integrated through LangChain. It provides a Streamlit UI to upload, index, and query PDF files with contextual understanding.

---

## 🚀 Features

- ✅ Upload a folder of PDFs and index them using FAISS
- ✅ Embed documents using **Amazon Titan Text Embeddings**
- ✅ Ask questions and get answers using:
  - `Claude (ai21.j2.mid-v1)`
  - `LLaMA2 (meta.llama2-70b-chat-v1)`
- ✅ Streamlit interface for ease of use

---

## 🧠 Architecture Overview

```plaintext
PDFs ──▶ LangChain Loader ──▶ Text Splitter ──▶ Titan Embeddings ──▶ FAISS Vector Store
                                                          │
                                                         ▼
                                      Amazon Bedrock (Claude / LLaMA2)
                                                          │
                                                         ▼
                                            🧠 Contextual Q&A Output
````

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/chat-pdf-bedrock.git
cd chat-pdf-bedrock
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up AWS credentials**
   Make sure your AWS credentials are configured correctly with access to Amazon Bedrock:

```bash
aws configure
```

4. **Create a `data/` folder and place your PDF files inside.**

---

## ▶️ Usage

```bash
streamlit run app.py
```

### Streamlit Sidebar

* **Update Vector Store**: Loads PDFs from `data/`, splits, and embeds using Amazon Titan and stores in FAISS.
* **Claude Output**: Uses Claude model to generate an answer.
* **LLaMA2 Output**: Uses LLaMA2 model to generate an answer.

---

## 🧾 Example

1. Place your PDFs inside the `/data` folder.
2. Click **"Vector Update"** to load and index.
3. Ask a question like:
   `"What are the key points in the document?"`
4. Choose your preferred model (`Claude` or `LLaMA2`) to get the response.

---

## 🧩 Technologies Used

* [Streamlit](https://streamlit.io/)
* [LangChain](https://www.langchain.com/)
* [Amazon Bedrock](https://aws.amazon.com/bedrock/)
* [FAISS](https://github.com/facebookresearch/faiss)
* Python 🐍

---

## ⚠️ Known Issues

* Ensure that the FAISS index folder is named `faiss_index` (currently a typo: `"fiass_index"` in code).
* Ensure Bedrock access is enabled in your AWS account.

---

## 📌 To-Do

* [ ] Support file upload via UI
* [ ] Improve formatting of answers
* [ ] Add support for multi-language documents


