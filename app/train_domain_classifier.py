# train_domain_classifier.py
import joblib
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

# Dummy training data (replace with real paper abstracts and labels)
X = [
    "Deep learning for image recognition",
    "Quantum entanglement in particles",
    "Neural network-based text summarization",
    "CRISPR gene editing techniques"
]
y = ["AI", "Physics", "AI", "Biology"]

# TF-IDF + Classifier Pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(X, y)

# Save classifier and vectorizer
joblib.dump(pipeline.named_steps['clf'], "assets/models/domain_classifier.pkl")
joblib.dump(pipeline.named_steps['tfidf'], "assets/models/vectorizer.pkl")

print("✅ Domain classifier and vectorizer saved.")
