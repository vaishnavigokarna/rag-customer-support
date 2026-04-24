def check_escalation(answer, context, results, query):

    if not results:
        return "⚠️ Escalated to Human Agent (No data found)"

    # check relevance
    query_words = query.lower().split()
    match = any(word in answer.lower() for word in query_words)

    if not match:
        return "⚠️ Escalated to Human Agent (Out of context)"

    if "not enough information" in answer.lower():
        return "⚠️ Escalated to Human Agent (Low confidence)"

    return answer