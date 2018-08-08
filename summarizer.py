#!/usr/bin/env python3

from functools import partial

from preprocessor import (
    process_text, remove_stopwords, tokenize_into_sentences
)

from textrank import textrank

import sys

def load_stopwords(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')

def load_file(filename):
    with open(filename) as f:
        return f.read().strip()

def summarize(text, topn=None):
    stop_words = load_stopwords('data/stopwords.txt')
    sentences = tokenize_into_sentences(text)

    topn = len(sentences)//3 if not topn else topn
    print("Generating top {} most relevant sentences out of {} total sentences".format(topn, len(sentences)))

    sentences_processed = list(map(process_text, sentences))
    remove_stop = partial(remove_stopwords, stop_words)
    sentences_tokenized = [ sentence for sentence in map(lambda x : remove_stop(x.split()), sentences_processed) if sentence]

    matrix, ranks = textrank(sentences_tokenized)
    res = []
    for tup in ranks[:topn]:
        idx = tup[0]
        res.append((sentences[idx], tup[1]))
    return res


def main():
    n = sys.argv[1:]
    n = int(n[0]) if n else None
    text = load_file('data/test')
    summary = summarize(text, topn=n)
    for s in summary:
        print(s)

if __name__ == "__main__":
    main()

