# config.py

import os

# Base directories
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, "data")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
MODELS_DIR = os.path.join(ASSETS_DIR, "models")
SAMPLE_PAPERS_DIR = os.path.join(ASSETS_DIR, "sample_papers")
EMBEDDING_PATH = os.path.join(DATA_DIR, "corpus_embeddings.pkl")

# Model paths
DOMAIN_CLASSIFIER_PATH = os.path.join(MODELS_DIR, "domain_classifier.pkl")

# Default options
SUMMARY_MAX_LENGTH = 150  # for summarizer
SUMMARY_MIN_LENGTH = 30
TOP_N_KEYWORDS = 20
PLAGIARISM_THRESHOLD = 0.75
TOP_K_MATCHES = 3

# Allowed file types for upload
ALLOWED_FILE_TYPES = [".pdf"]

# Streamlit page config
APP_TITLE = "📚 Research Paper Analyzer Pro"
APP_DESCRIPTION = "An AI-powered tool to analyze, summarize, classify, and evaluate research papers."
APP_ICON = "📖"
