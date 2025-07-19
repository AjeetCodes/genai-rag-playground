# 🧠 genai-rag-playground

A personal learning playground for building and experimenting with **Generative AI**, **RAG (Retrieval-Augmented Generation)** pipelines, and **Streamlit-based user interfaces**.

This repo includes multiple mini-projects and prototypes that demonstrate how to combine **LLMs**, **vector search**, and **external data sources** to create smart, context-aware applications.

---

## 🚀 Projects

| Folder | Description |
|--------|-------------|
| `simple-rag-app/` | Minimal RAG app using LangChain, Streamlit, and local documents |
| `streamlit-rag-app/` | UI experiments: layouts, widgets, rag-app & multi-page setup |
| `chromadb-experiments/` | quick start of vector db(chroma) |
<!-- | `youtube-chat-app/` | Ask questions about a YouTube video by extracting its transcript and running RAG | -->
<!-- | `components/` | Reusable Python modules: vector store, embeddings, prompts, etc. | -->
<!-- | `notebooks/` | Jupyter notebooks for testing LangChain, LLMs, and vector similarity search | -->

---

## 🔧 Tech Stack

- 🧩 LangChain
- 🧠 LLMs: OpenAI GPT-4, Gemini Pro, Claude (configurable)
- 📄 Vector DBs: ChromaDB
- 🌐 Streamlit
<!-- - 📺 YouTube Transcript API -->
- 📦 Python 3.10+

---

## 📦 Installation

```bash
# Clone the repo
git clone git@github-personal:ajeetcodes/genai-rag-playground.git
cd genai-rag-playground

# Create and activate virtual environment
python -m venv app-env
source app-env/bin/activate  # Windows: app-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

