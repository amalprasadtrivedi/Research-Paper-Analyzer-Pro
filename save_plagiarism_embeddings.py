# save_plagiarism_embeddings.py
import os
import pickle
from sentence_transformers import SentenceTransformer
from backend_services import pdf_parser

model = SentenceTransformer('all-MiniLM-L6-v2')

pdf_folder = "assets/sample_papers/"
corpus = []
filenames = []

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        text = pdf_parser.extract_text_from_pdf(os.path.join(pdf_folder, filename))
        if text:
            corpus.append(text)
            filenames.append(filename)

embeddings = model.encode(corpus, show_progress_bar=True)

with open("assets/models/plagiarism_corpus.pkl", "wb") as f:
    pickle.dump(embeddings, f)

with open("assets/models/plagiarism_filenames.pkl", "wb") as f:
    pickle.dump(filenames, f)

print("✅ Plagiarism embeddings and filenames saved.")
