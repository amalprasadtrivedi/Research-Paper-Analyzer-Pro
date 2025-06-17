# save_embedding_model.py
from sentence_transformers import SentenceTransformer

model_name = "all-MiniLM-L6-v2"
save_path = "assets/models/embedding_model/"

model = SentenceTransformer(model_name)
model.save(save_path)

print(f"✅ Embedding model saved to {save_path}")
