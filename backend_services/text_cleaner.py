# text_cleaner.py

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure required resources are downloaded
nltk.download("punkt")
nltk.download("stopwords")

# Initialize stopwords set
STOPWORDS = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    """
    Cleans and preprocesses the input text.

    Steps:
    - Lowercasing
    - Removing special characters, numbers, extra spaces
    - Tokenizing
    - Removing stopwords

    Args:
        text (str): Raw text input.

    Returns:
        str: Cleaned text.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove special characters and digits
    text = re.sub(r"[^a-z\s]", "", text)

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered_tokens = [word for word in tokens if word not in STOPWORDS and len(word) > 2]

    # Join back into cleaned string
    cleaned_text = " ".join(filtered_tokens)

    return cleaned_text
