from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer("all-MiniLM-L6-v2")
sentences = [
    "I am studying computer science.",
    "I am learning programming.",
    "Python is a popular programming language.",
    "I enjoy watching movies.",
    "The new movie was very interesting.",
    "I like playing cricket.",
    "Artificial intelligence is useful in many fields.",
    "Machine learning helps computers learn from data."
]
embeddings = model.encode(sentences)
print("Total number of sentences:", len(sentences))
print("Embedding dimension:", len(embeddings[0]))
print("\n--- Sentence Embeddings ---")

for i, sentence in enumerate(sentences):
    print("\nSentence", i + 1, ":", sentence)
    print("Embedding:", embeddings[i])
similarity = cosine_similarity(embeddings)

print("\n--- Semantic Similarity ---")

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):

        score = similarity[i][j]

        if score > 0.5:
            print("\nSentence 1:", sentences[i])
            print("Sentence 2:", sentences[j])
            print("Similarity:", round(score, 4))

print("\n--- Completed ---")
print("Similar sentences are identified using cosine similarity.")
