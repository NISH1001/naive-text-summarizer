#!/usr/bin/env python3
import re

def process_text(text):
    text = text.encode('ascii', errors='ignore').decode()
    text = re.sub(r"’", "'", text)
    text = re.sub(r"“", ' " ', text)
    text = text.lower()
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r"([A-Za-z]+)'s", r"\1 is", text)

    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)

    text = re.sub(r"dont", " do not", text)
    text = re.sub(r"didnt", " did not", text)
    text = re.sub(r"wont", " will not", text)
    text = re.sub(r"cant", " can not", text)
    text = re.sub(r"shouldnt", " should not", text)

    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'s", " is ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r'\W', ' ', text)
    # text = re.sub(r'\d+', ' <number> ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def remove_stopwords(stopwords, tokens):
    res = []
    for token in tokens:
        if not token in stopwords:
            res.append(token)
    return res

def tokenize_into_sentences(text):
    regex = "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"
    return [ sentence.strip() for sentence in re.split(regex, text) if sentence]


def main():
    text = "there's something i need to know. my name is Paradox. I am Mr. Paradox."
    sentences = tokenize_into_sentences(text)
    print(sentences)
    # print(process_text(text))

if __name__ == "__main__":
    main()

