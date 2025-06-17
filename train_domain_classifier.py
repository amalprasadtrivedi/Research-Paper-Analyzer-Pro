import joblib
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

# Training data
X = [
    "Deep learning for image recognition",
    "Quantum entanglement in particles",
    "Neural network-based text summarization",
    "CRISPR gene editing techniques"
]
y = ["AI", "Physics", "AI", "Biology"]

# Full pipeline = vectorizer + classifier
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(X, y)

# ✅ Save entire pipeline
joblib.dump(pipeline, "assets/models/domain_pipeline.pkl")
print("✅ Full domain pipeline saved.")
