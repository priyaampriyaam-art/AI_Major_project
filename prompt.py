def get_prompt():
    prompt_template = """
    You are a helpful AI assistant. Answer the question based only on the given context.
    If you don't know the answer from context, say "I don't know from given documents".
    
    Context: {context}
    Question: {question}
    
    Answer:
    """
    return prompt_template