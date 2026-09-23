# Embedding Models

## Overview

This project demonstrates how text can be converted into numerical vector representations using a pre-trained Sentence Transformer model. These vectors are called **embeddings** and can be used to represent the meaning of text in a form that a computer can process.


## Technologies Used

* Python
* Sentence Transformers
* NumPy

## Project Files

```text
Embedding-Models/
│
├── embedding.py
├── output.txt
└── README.md
```



## Example

### Input

```text
I love learning Artificial Intelligence.
```

### Output

```text
Embedding vector:
[0.0123, -0.0456, 0.0789, ...]
```

The actual output contains many numerical values because the text is represented as a vector.

## Features

* Converts text into numerical embeddings
* Uses a pre-trained Sentence Transformer model
* Simple Python implementation
* Easy to understand for beginners
* Can be extended to text similarity and semantic search

## Applications

Text embeddings are commonly used in:

* Text similarity
* Semantic search
* Recommendation systems
* Question answering
* Document comparison
* Information retrieval
* Natural Language Processing (NLP)


## Learning Outcome

Through this project, I learned how embedding models represent text as numerical vectors and how these representations can be used as a foundation for different Natural Language Processing applications.

## Conclusion

This project provides a basic understanding of text embeddings using Sentence Transformers. It demonstrates how simple text input can be converted into numerical representations that can later be used for more advanced NLP tasks.
