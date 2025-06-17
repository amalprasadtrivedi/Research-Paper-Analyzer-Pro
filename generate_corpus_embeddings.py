from sentence_transformers import SentenceTransformer
import joblib
import os

# Sample corpus texts (replace these with real abstracts in production)
corpus_texts = [
    "Deep learning for image recognition",
    "Quantum entanglement in particles",
    "Neural network-based text summarization",
    "CRISPR gene editing techniques"
]

# Load the same model used in plagiarism_checker.py
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate sentence embeddings
corpus_embeddings = model.encode(corpus_texts)

# Ensure directory exists
os.makedirs("assets/models", exist_ok=True)

# Save as dictionary with required structure
joblib.dump({
    "texts": corpus_texts,
    "embeddings": corpus_embeddings
}, "assets/models/corpus_embeddings.pkl")

print("✅ Embeddings file created successfully.")
