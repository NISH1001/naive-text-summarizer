#!/usr/bin/env python3

import numpy as np

def build_index(pagemap):
    pages = pagemap.keys()
    return { page: idx for idx, page in enumerate(pages) }


def build_transition_matrix(pagemap, indices):
    n = len(indices)
    transition = np.zeros((n,n))
    total_links = 0
    # for each page, find probability of transition to other page
    for source_page in pagemap:
        destinations = pagemap[source_page]
        i = indices[source_page]
        if not destinations:
            transition[i] = np.ones(n)/n
        else:
            for dest_page in destinations:
                j = indices[dest_page]
                total_links += 1
                transition[i][j] = 1/len(pagemap[source_page])
    return transition

def pagerank(matrix, eps=0.0001, d=0.85):
    n = len(matrix)
    probs = np.ones(n)/n
    for i in range(4):
        new_p = np.ones(n) * (1-d)/n + d*matrix.T.dot(probs)
        delta = abs(new_p-probs).sum()
        if delta <= eps:
            break
        probs = new_p
    return sorted(enumerate(new_p), key=lambda x: -x[1])


def main():
    links = {
        'webpage-1': set(['webpage-2', 'webpage-4', 'webpage-5', 'webpage-6', 'webpage-8', 'webpage-9', 'webpage-10']),
        'webpage-2': set(['webpage-5', 'webpage-6']),
        'webpage-3': set(['webpage-10']),
        'webpage-4': set(['webpage-9']),
        'webpage-5': set(['webpage-2', 'webpage-4']),
        'webpage-6': set([]),
        'webpage-7': set(['webpage-1', 'webpage-3', 'webpage-4']),
        'webpage-8': set(['webpage-1']),
        'webpage-9': set(['webpage-1', 'webpage-2', 'webpage-3', 'webpage-8', 'webpage-10']),
        'webpage-10': set(['webpage-2', 'webpage-3', 'webpage-8', 'webpage-9']),
    }
    print(links)
    indices = build_index(links)
    transition = build_transition_matrix(links, indices)
    print("Transition matrix :: ")
    print(transition)

    results= pagerank(transition)
    print("Page rank result :: ")
    print(results)

if __name__ == "__main__":
    main()

