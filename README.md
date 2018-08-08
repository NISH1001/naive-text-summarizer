# naive-text-summarizer
A naive text summarizer written from scratch using text rank algorithm

## Requirements
All you need is python version 3+ and numpy. Install numpy using **pip** for python3 as:
```bash
pip install numpy
```



## Under The Hood (textrank Algorithm)
Textrank algorithm is one of the simplest (and the coolest) algorithms to implement text summarization method. 
The concept is derived from the infamous pagerank algorithm, where instead of web pages we have sentences. 
And the probability of transition from one sentence to another is just the similarity between them. 
So, think of outbound links as a similarity metric between corresponding sentences. 
And using this transition matrix, we compute the ranks of each sentence.

It's simple as that. Once you can understand that intuitively, it makes sense in terms of summarization. 
We get the ranks and use the sentences having higher ranks.
Intuitively, it is nothing but choosing some "important" and "similar" sentences from the list of sentences that will, 
in some ways, represent the whole text.

**cosine similarity**
The cosine similarity is nothing but the cosine of angle between the two vectors. 
This is directly derived from the dot product.  
Say we have two vectors **v1** and **v2**. The dot product is defined as:

```bash
dot(v1, v2) = |v1| * |v2| * cos(theta)
```

where,
theta = angle between the two vectors

From here, cos(theta) gives us the cosine similarity. 


**pagerank**
PageRank algorithm, in its simplest form, works by finding the probability (count) of transition from one web page to another.  
This is generally represented by a transition matrix, which is a square matrix wth values representing the probabilities from 
one state to another. This is directly reduced from the total number of outbound links from current webpage.

**textrank**
TextRank algorithm is one of the simplest (and the coolest) algorithms to implement text summarization method.  
It makes use of the aforementioned **pagerank** algorithm where instead of web pages we have sentences. 
And the probability of transition from one sentence to another is just the similarity between them. 
So, think of outbound links as a similarity metric between corresponding sentences. 
And using this transition matrix, we compute the ranks of each sentence.

It's simple as that. Once you can understand that intuitively, it makes sense in terms of summarization. 
We get the ranks and use the sentences having higher ranks.
Intuitively, it is nothing but choosing some "important" and "similar" sentences from the list of sentences that will, in some ways, 
represent the whole text.

## Usage
Run the summarizer module:  

```bash
python summarizer.py
```

This expects you to have a file named **test** inside **data/** folder i.e. **data/test** file is read and summarized accordingly.
