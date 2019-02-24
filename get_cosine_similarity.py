def get_cosine_similarity(tfidf_matrix):

    return list(np.diag(cosine_similarity(tfidf_matrix, tfidf_matrix), k=1))

def get_cosine_similarity(tfidf_matrix):

    cosine_matrix = cosine_similarity(tfidf_matrix)
    return (cosine_matrix[0][1::].tolist())
