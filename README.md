# 🤖 RAG Customer Support Assistant

## 📌 Project Overview

This project is a **Retrieval-Augmented Generation (RAG) based Customer Support Assistant** built using **LangChain, LangGraph, and Streamlit**.

It answers user queries based on a **PDF knowledge base** (customer support policies) instead of generating random answers.

---

## 🎯 Objective

To build an intelligent assistant that:

* Retrieves relevant information from documents
* Provides accurate answers using context
* Avoids hallucination (wrong answers)
* Escalates to human agent if answer is weak

---

## 🛠️ Technologies Used

* Python
* Streamlit (Web UI)
* LangChain
* LangGraph
* ChromaDB (Vector Database)
* Sentence Transformers (Embeddings)
* PyPDF (Document Loader)

---

## 📂 Project Structure

```
RAG_LangGraph_project/
│
├── data/
│   └── document.pdf
│
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── llm.py
│   ├── workflow.py
│   └── hitl.py
│
├── app.py
└── README.md
```

---

## ⚙️ How It Works

1. **Load PDF**

   * Reads customer support document

2. **Chunking**

   * Splits text into smaller parts

3. **Embeddings**

   * Converts text into vectors

4. **Vector Database**

   * Stores embeddings in ChromaDB

5. **Retriever**

   * Finds relevant chunks based on query

6. **LLM Processing**

   * Generates answer using retrieved context

7. **Human Escalation**

   * If answer is weak → Escalate to human

---

## 🚀 How to Run the Project

### Step 1: Install dependencies

```bash
python -m pip install langchain langchain-community chromadb pypdf sentence-transformers transformers accelerate langgraph streamlit
```

---

### Step 2: Run the app

```bash
python -m streamlit run app.py
```

---

### Step 3: Open in browser

```
http://localhost:8501
```

---

## 💡 Example Questions

* What is refund policy?
* How long does delivery take?
* How to reset password?
* What are payment methods?
* How to track my order?

---

## ⚠️ Important Note

* The system answers **ONLY from the PDF**
* If answer is not found → shows:

  > "We don't have enough information"

---

## 📽️ Demo Features

* User-friendly interface
* Real-time question answering
* Context-based responses
* Human escalation for weak answers

---

## 🔮 Future Improvements

* Add voice input
* Connect real APIs
* Improve UI design
* Add multiple documents support

---

## 📌 Conclusion

This project demonstrates how **RAG architecture** can improve accuracy in AI systems by combining **retrieval + generation**, making it useful for real-world applications like customer support.
