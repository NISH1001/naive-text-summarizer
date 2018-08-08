#!/usr/bin/env python3

from functools import partial
import numpy as np

from pagerank import pagerank

def magnitude(vec):
    return np.linalg.norm(vec)

def calculate_similarity(tokens1, tokens2):
    vocab = set(tokens1 + tokens2)
    n = len(vocab)
    v1, v2 = [], []
    for word in vocab:
        v1.append(int(word in tokens1))
        v2.append(int(word in tokens2))
    return np.dot(v1, v2)/(magnitude(v1) * magnitude(v2))

def build_sim_matrix(sentences_tokenized):
    n = len(sentences_tokenized)
    matrix = np.ones((n, n))
    for i, sent1 in enumerate(sentences_tokenized):
        for j, sent2 in enumerate(sentences_tokenized):
            sim = calculate_similarity(sent1, sent2)
            matrix[i][j] = sim
            matrix[j][i] = sim
    return matrix

def textrank(sentences_tokenized, topn=5):
    matrix = build_sim_matrix(sentences_tokenized)
    ranks = pagerank(matrix)
    return ranks

def main():

    sentences = [
        "i am paradox",
        "my name is paradox",
        "i love caffeine"
    ]
    sentences_tokenized = list(map(lambda x : x.split(), sentences))
    print(sentences_tokenized)
    matrix = build_sim_matrix(sentences_tokenized)
    print(matrix)
    result = pagerank(matrix)
    print(result)


if __name__ == "__main__":
    main()

