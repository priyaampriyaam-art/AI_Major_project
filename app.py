import streamlit as st
from rag_pipeline import get_answer

st.set_page_config(page_title="AI Major Project - RAG System", layout="wide")

st.title("📚 AI Major Project - Document Q&A")
st.write("Ask questions from your documents!")

question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question:
        with st.spinner("Searching in documents..."):
            answer, source_docs = get_answer(question)
            st.success("Answer found!")
            st.write(answer)
            
            with st.expander("See Source Documents"):
                for i, doc in enumerate(source_docs):
                    st.write(f"**Source {i+1}:**")
                    st.write(doc.page_content)
                    st.divider()
    else:
        st.warning("Please enter a question!")

st.sidebar.title("About")
st.sidebar.info("This is a RAG system using ChromaDB and HuggingFace embeddings. No OpenAI key needed.")