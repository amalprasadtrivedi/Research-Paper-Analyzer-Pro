# embedder.py

from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

# Load the model only once when this script is imported
model = SentenceTransformer("all-MiniLM-L6-v2")  # Lightweight & fast; great for semantic tasks

def get_embedding(text: str) -> np.ndarray:
    """
    Returns the sentence embedding for a single string.

    Args:
        text (str): Input text (sentence or paragraph).

    Returns:
        np.ndarray: 384-dimensional embedding vector.
    """
    return model.encode(text)

def get_embeddings(text_list: List[str]) -> np.ndarray:
    """
    Returns sentence embeddings for a list of strings.

    Args:
        text_list (List[str]): List of text samples.

    Returns:
        np.ndarray: 2D array where each row is an embedding vector.
    """
    return model.encode(text_list, show_progress_bar=True)


def get_sentence_embeddings(text):
    """
    Converts input text into a vector embedding using SBERT.
    If the text is long, it will process it in a single chunk.
    """
    try:
        return sbert_model.encode(text, convert_to_tensor=False)  # numpy array
    except Exception as e:
        print(f"❌ Failed to embed text: {e}")
        return None