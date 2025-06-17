# domain_classifier.py

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from typing import Tuple, List
import os

from app.train_domain_classifier import pipeline

# Define path to save or load model
MODEL_PATH = "assets/models/domain_classifier.pkl"

# Define some example domains and dummy data (can be replaced with real dataset)
example_data = [
    ("Neural networks and deep learning in image recognition", "Computer Science"),
    ("DNA sequencing and genome mapping technologies", "Biology"),
    ("Quantum entanglement and wave-particle duality experiments", "Physics"),
    ("Machine learning algorithms for fraud detection", "Computer Science"),
    ("Photosynthesis and chlorophyll absorption process", "Biology"),
    ("String theory and quantum field equations", "Physics")
]

def train_classifier(data: List[Tuple[str, str]], save_model: bool = True) -> Pipeline:
    """
    Trains a TF-IDF + Logistic Regression classifier to predict domain labels.

    Args:
        data (List[Tuple[str, str]]): List of (text, label) pairs.
        save_model (bool): If True, saves the model to disk.

    Returns:
        Pipeline: Trained sklearn pipeline.
    """
    texts, labels = zip(*data)

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english", max_features=5000)),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(texts, labels)

    if save_model:
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        joblib.dump(pipeline, MODEL_PATH)

    return pipeline

def load_classifier() -> Pipeline:
    """
    Loads a trained classifier from disk.

    Returns:
        Pipeline: Loaded sklearn pipeline.
    """
    if not os.path.exists(MODEL_PATH):
        # If not trained, fallback to dummy training
        return train_classifier(example_data)
    return joblib.load(MODEL_PATH)

def predict_domain(text: str) -> str:
    """
    Predicts the domain/field of a given research text.

    Args:
        text (str): Input research paper abstract or content.

    Returns:
        str: Predicted domain.
    """
    model = load_classifier()
    prediction = model.predict([text])[0]
    return prediction


def classify_paper(text):

    """
    Classify the domain of the paper.
    Ensures the text is a string and passed as a list to the pipeline.
    """

    """
    if not isinstance(text, str):
        text = str(text)

    try:
        prediction = pipeline.predict([text])  # Works because tfidf is inside
        return prediction[0]
    except Exception as e:
        print(f"❌ Classification Error: {str(e)}")
        return "Unknown"
    
    """
    try:
        return pipeline.predict([text])[0]
    except Exception as e:
        print(f"[ERROR] in classify_paper: {e}")
        return "Unknown"