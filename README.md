
# 🧠 Research Paper Analyzer Pro

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-%23FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

## 📚 Overview

**Research Paper Analyzer Pro** is an advanced Machine Learning and AI-powered application designed to assist researchers, students, and academicians in analyzing research papers with high accuracy. It provides domain classification, keyword extraction, summary generation, plagiarism detection, and more — all in a user-friendly web application powered by **Streamlit**.

---

## ✨ Features

- 🔍 **Domain Classification** — Identifies the field of research (e.g., AI, Physics, Biology)
- 📌 **Keyword Extraction** — Extracts important keywords from the paper
- 📝 **Summary Generation** — Summarizes the research paper using NLP techniques
- ⚠️ **Plagiarism Detection** — Compares paper against a database to check for similarity
- 📥 **PDF Upload & Viewer** — Upload your paper and view it inside the app
- 📊 **Explainable AI** — Understand AI decisions with transparency

---

## 🚀 Demo

> Streamlit app interface showing PDF preview, NLP-based insights, and visual components.

*(Include screenshots here)*

---

## 📁 Project Structure

```
Research-Paper-Analyzer-Pro/
│
├── app/
│   ├── main.py                   # Streamlit App
│   └── config.py                 # App configurations
│
├── assets/
│   └── models/                   # Trained ML models and embeddings
│       ├── domain_classifier.pkl
│       └── vectorizer.pkl
│
├── modules/
│   ├── domain_classifier.py      # Domain classification logic
│   ├── plagiarism_checker.py     # Semantic plagiarism detection
│   ├── summarizer.py             # Paper summarization
│   ├── keyword_extractor.py      # RAKE keyword extraction
│   └── utils.py                  # Utility functions
│
├── train/
│   ├── train_domain_classifier.py
│   └── build_embeddings.py
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Installation

### ✅ Requirements

- Python >= 3.10
- pip

### 🐍 Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📤 How to Run

```bash
streamlit run app/main.py
```

After running, the app will open in your browser.

---

## 🔍 Module Descriptions

### 1️⃣ Domain Classifier

- Uses **TF-IDF + Logistic Regression**
- Trained on abstracts from diverse research fields
- Predicts the domain: AI, Physics, Biology, etc.

```python
# Usage
from modules.domain_classifier import classify_paper
result = classify_paper("Your research paper abstract here")
```

### 2️⃣ Keyword Extractor

- Implements **RAKE (Rapid Automatic Keyword Extraction)**
- Extracts key phrases to give semantic overview

### 3️⃣ Summarizer

- Uses **HuggingFace Transformers**
- Models like `distilbart-cnn-12-6` to summarize paragraphs

### 4️⃣ Plagiarism Checker

- Uses **SBERT** for sentence embeddings
- Calculates **cosine similarity**
- Matches input against existing paper embeddings

```python
from modules.plagiarism_checker import check_plagiarism
matches = check_plagiarism("research content")
```

---

## 🧪 Example Usage

```python
# Example to classify paper
from modules.domain_classifier import classify_paper
result = classify_paper("Deep Learning in Military Applications")

# Example to check plagiarism
from modules.plagiarism_checker import check_plagiarism
matches = check_plagiarism("Some abstract", threshold=0.75)
```

---

## 🧠 Models & Training

You can retrain the classifier using:

```bash
python train/train_domain_classifier.py
```

You can also generate corpus embeddings for plagiarism detection using:

```bash
python train/build_embeddings.py
```

Ensure you have `corpus_texts.pkl` with text entries in your corpus before building.

---

## 🧩 Technologies Used

| Technology        | Purpose                     |
|-------------------|-----------------------------|
| Python 🐍         | Core Programming Language   |
| Streamlit 🔴       | Web UI Framework            |
| scikit-learn ⚙️    | ML model building           |
| SentenceTransformers 🧠 | Semantic embeddings       |
| HuggingFace 🤗     | Text Summarization Model    |
| NumPy 📐          | Vector calculations         |

---

## 📂 Sample Data Format

For domain classification, training data is in format:

```python
X = ["Paper abstract 1", "Paper abstract 2", ...]
y = ["AI", "Physics", ...]
```

For plagiarism:

- Save texts and their embeddings into a `dict` and use `joblib.dump(...)` to `corpus_embeddings.pkl`.

---

## 💡 Future Enhancements

- ✍️ Support for **multiple file upload**
- 🧬 Add **semantic topic modeling**
- 📈 Add analytics dashboard (plots/graphs)
- 🔐 Add user authentication & cloud support

---

## ❓ FAQ

### 1. Can I upload a `.docx` file?
No, currently only `.pdf` files are supported.

### 2. How is plagiarism checked?
We use **cosine similarity** on SBERT sentence embeddings.

### 3. How do I add more domains?
Add new labeled data in `train/train_domain_classifier.py` and retrain.

---

## 🧑‍💻 Contributors

- **Amal Prasad Trivedi** – Developer, ML Engineer  
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/amal-prasad-trivedi-b47718271/)  
  [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/amalprasadtrivedi)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- 🤗 HuggingFace for their NLP models
- 🧠 SBERT team for semantic sentence embeddings
- 🎯 Streamlit for providing an easy-to-use UI framework

---

## 🗂️ Resources & References

- [SBERT Documentation](https://www.sbert.net/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-Learn Docs](https://scikit-learn.org/)
- [RAKE Algorithm](https://pypi.org/project/rake-nltk/)

---

**Made with ❤️ for researchers and students by Amal Prasad Trivedi.**
