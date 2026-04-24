def get_results(db, query):
    return db.similarity_search(query, k=3)