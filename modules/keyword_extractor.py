# keyword_extractor.py

from sklearn.feature_extraction.text import TfidfVectorizer
from rake_nltk import Rake
from typing import List, Tuple, Literal
import nltk

nltk.download('stopwords')
nltk.download('punkt')


def extract_keywords_tfidf(text: str, top_n: int = 20) -> List[Tuple[str, float]]:
    """
    Extracts top N keywords using TF-IDF.

    Args:
        text (str): Input document.
        top_n (int): Number of keywords to return.

    Returns:
        List[Tuple[str, float]]: List of (keyword, score)
    """
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([text])
    scores = tfidf_matrix.toarray()[0]
    keywords = vectorizer.get_feature_names_out()

    scored_keywords = list(zip(keywords, scores))
    sorted_keywords = sorted(scored_keywords, key=lambda x: x[1], reverse=True)

    return sorted_keywords[:top_n]


def extract_keywords_rake(text: str, top_n: int = 20) -> List[Tuple[str, float]]:
    """
    Extracts top N keywords/phrases using RAKE.

    Args:
        text (str): Input document.
        top_n (int): Number of keywords to return.

    Returns:
        List[Tuple[str, float]]: List of (phrase, score)
    """
    rake = Rake()
    rake.extract_keywords_from_text(text)
    ranked_phrases = rake.get_ranked_phrases_with_scores()

    return ranked_phrases[:top_n]


def extract_keywords(
    text: str,
    method: Literal["tfidf", "rake"] = "tfidf",
    top_n: int = 20
) -> List[Tuple[str, float]]:
    """
    Unified keyword extraction interface.

    Args:
        text (str): Input document.
        method (str): 'tfidf' or 'rake'.
        top_n (int): Top N keywords to extract.

    Returns:
        List[Tuple[str, float]]: List of (keyword/phrase, score)
    """
    if len(text.strip().split()) < 20:
        return []

    if method == "tfidf":
        return extract_keywords_tfidf(text, top_n)
    elif method == "rake":
        return extract_keywords_rake(text, top_n)
    else:
        raise ValueError("Method must be either 'tfidf' or 'rake'")
