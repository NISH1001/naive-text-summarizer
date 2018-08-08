#!/usr/bin/env python3

from functools import partial

from preprocessor import (
    process_text, remove_stopwords, tokenize_into_sentences
)

from textrank import textrank

def load_stopwords(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')

def load_file(filename):
    with open(filename) as f:
        return f.read().strip()

def summarize(text, topn=5):
    stop_words = load_stopwords('data/stopwords.txt')
    sentences = tokenize_into_sentences(text)
    sentences = list(map(process_text, sentences))
    remove_stop = partial(remove_stopwords, stop_words)
    sentences_tokenized = list(map(lambda x : remove_stop(x.split()), sentences))

    matrix, ranks = textrank(sentences_tokenized)
    res = []
    # topn = len(sentences)//3
    for tup in ranks[:topn]:
        idx = tup[0]
        res.append((sentences[idx], tup[1]))
    return res


def main():
    text = load_file('data/test')
    summary = summarize(text, 6)
    for s in summary:
        print(s)

if __name__ == "__main__":
    main()

