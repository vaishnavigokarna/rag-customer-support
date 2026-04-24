import streamlit as st

st.title("🤖 RAG Customer Support Assistant")

try:
    from src.loader import load_pdf
    from src.chunker import chunk_docs
    from src.embeddings import create_db
    from src.workflow import build_graph

    @st.cache_resource
    def load_system():
        docs = load_pdf("data/document.pdf")
        chunks = chunk_docs(docs)
        db = create_db(chunks)
        app = build_graph(db)
        return app

    app_graph = load_system()

    query = st.text_input("Ask a question:")

    if st.button("Get Answer"):
        if query.strip() == "":
            st.warning("Enter a question")
        else:
            result = app_graph.invoke({
                "query": query,
                "answer": ""
            })
            st.write(result["answer"])

except Exception as e:
    st.error("Error occurred:")
    st.text(str(e))