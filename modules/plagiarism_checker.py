# plagiarism_checker.py

from typing import List, Tuple
import numpy as np
import os
import pickle
from sentence_transformers import SentenceTransformer, util
from torch import Tensor
from joblib import load

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Path to embeddings
EMBEDDINGS_PATH = "assets/models/corpus_embeddings.pkl"


def compute_embedding(text: str) -> Tensor:
    """
    Compute SBERT embedding for input text.
    """
    return model.encode(text, convert_to_tensor=True)


def load_corpus_embeddings() -> Tuple[List[str], np.ndarray]:
    """
    Load embeddings and texts from a pickle file.
    Returns:
        texts: list of stored paper texts
        embeddings: 2D numpy array of sentence embeddings
    """
    if not os.path.exists(EMBEDDINGS_PATH):
        raise FileNotFoundError(f"❌ Embedding file not found: {EMBEDDINGS_PATH}")

    try:
        with open(EMBEDDINGS_PATH, "rb") as f:
            data = load(EMBEDDINGS_PATH)
    except Exception as e:
        raise ValueError(f"❌ Could not load embeddings file: {e}")

    if "texts" not in data or "embeddings" not in data:
        raise KeyError("❌ Embedding file must contain both 'texts' and 'embeddings' keys.")

    texts = data["texts"]
    embeddings = data["embeddings"]

    if not isinstance(embeddings, np.ndarray):
        embeddings = np.array(embeddings)

    return texts, embeddings


def check_plagiarism(text: str, threshold: float = 0.75, top_k: int = 3) -> List[Tuple[str, float]]:
    """
    Check for plagiarism using cosine similarity.
    Returns:
        List of (matched_text, similarity_score)
    """
    if top_k <= 0:
        raise ValueError("⚠️ 'top_k' must be greater than 0.")

    corpus_texts, corpus_embeddings = load_corpus_embeddings()

    if len(corpus_texts) == 0 or corpus_embeddings.shape[0] == 0:
        raise ValueError("⚠️ Empty corpus embeddings.")

    # Compute embedding of input
    input_embedding = compute_embedding(text)

    # Compute cosine similarity
    similarities = util.cos_sim(input_embedding, corpus_embeddings)[0].cpu().numpy()

    # Sort by similarity
    sorted_indices = np.argsort(similarities)[::-1]

    # Get top_k matches over threshold
    matches = []
    for idx in sorted_indices[:top_k]:
        score = float(similarities[idx])
        if score >= threshold:
            matches.append((corpus_texts[idx], score))

    return matches
