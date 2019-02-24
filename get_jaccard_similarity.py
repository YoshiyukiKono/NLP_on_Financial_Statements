def get_jaccard_similarity(bag_of_words_matrix):

    similarities = []
    for bag_of_words_i in range(len(bag_of_words_matrix) - 1):
        similarities.append(jaccard_similarity_score(
            bag_of_words_matrix[bag_of_words_i].astype(bool),
            bag_of_words_matrix[bag_of_words_i + 1].astype(bool)))

    return similarities
