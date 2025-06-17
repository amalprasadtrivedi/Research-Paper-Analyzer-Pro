# save_keyword_model.py
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "Deep learning is transforming AI research",
    "Quantum mechanics and entanglement are core to physics",
    "DNA sequencing and genome editing help biology advance"
]

vectorizer = TfidfVectorizer(max_features=20)
vectorizer.fit(docs)

joblib.dump(vectorizer, "assets/models/keyword_model.pkl")
print("✅ Keyword vectorizer saved.")
