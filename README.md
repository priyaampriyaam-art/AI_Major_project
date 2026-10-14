# Domain-Specific RAG Chatbot - PDF Question Answering

Build a chatbot that answers questions ONLY from uploaded PDFs with sources and refuses when not found.

## Workflow (As per PDF Page 3)
Upload PDF -> Extract Text (pypdf) -> Split into chunks (800 chars, 100 overlap) -> Embeddings (all-MiniLM-L6-v2) -> Store in FAISS -> User asks question -> Retrieve top 3 chunks -> LLM generates grounded answer with source

## Tools Used
Python, pypdf, LangChain, sentence-transformers (all-MiniLM-L6-v2), FAISS, Streamlit

## How to Run
pip install -r requirements.txt
streamlit run app.py

## Features Covered (PDF Page 4)
1. PDF Upload
2. Text extraction & chunking
3. Embeddings
4. FAISS vector store & search
5. Answer from documents only
6. Source + page display
7. Refuse when not found
8. Streamlit UI
9. GitHub + README + Tests

## Responsible AI
- .env file excluded via .gitignore (no API keys exposed)
- System verifies info from original docs only
- Prompt injection protection: ignores instructions inside documents