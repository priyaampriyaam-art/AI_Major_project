from loader import load_documents
from vector_store import create_vector_store, load_vector_store
from prompt import get_prompt
import os

def get_answer(question):
    # Check if vector store exists
    if not os.path.exists("vector_store/saved_index") or len(os.listdir("vector_store/saved_index")) == 0:
        print("Creating new vector store...")
        chunks = load_documents()
        vectordb = create_vector_store(chunks)
    else:
        vectordb = load_vector_store()

    # Search
    docs = vectordb.similarity_search(question, k=2)
    
    # Combine context
    context = "\n\n".join([d.page_content for d in docs])
    
    # Simple answer from context (no API key needed)
    prompt_template = get_prompt()
    final_prompt = prompt_template.format(context=context, question=question)
    
    # For demo, we return context as answer - in college you can show this
    if context:
        answer = f"Based on your documents:\n\n{context}\n\n---\nQuestion was: {question}"
    else:
        answer = "I don't know from given documents"
    
    return answer, docs