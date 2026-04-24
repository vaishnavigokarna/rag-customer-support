def generate_answer(results, query):

    if not results:
        return "⚠️ I don't have enough information.", ""

    # Combine top results
    context = " ".join([doc.page_content for doc in results])

    # Extract only relevant sentence
    lines = context.split(".")
    
    for line in lines:
        if "refund" in query.lower() and "refund" in line.lower():
            return line.strip() + ".", context
        if "shipping" in query.lower() and "shipping" in line.lower():
            return line.strip() + ".", context
        if "contact" in query.lower() and ("contact" in line.lower() or "email" in line.lower()):
            return line.strip() + ".", context

    # fallback
    return context.split(".")[0] + ".", context