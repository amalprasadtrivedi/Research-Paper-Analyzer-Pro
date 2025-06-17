# summarizer.py

from typing import Literal
import nltk
import warnings

warnings.filterwarnings("ignore")
nltk.download("punkt")

# Optional: For extractive TextRank method
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Transformer-based abstractive summarization
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load model once
t5_model = T5ForConditionalGeneration.from_pretrained("t5-small")
t5_tokenizer = T5Tokenizer.from_pretrained("t5-small")

def summarize_with_t5(text: str, max_length: int = 150) -> str:
    """
    Summarizes text using T5 transformer.

    Args:
        text (str): Raw input text.
        max_length (int): Maximum tokens in output summary.

    Returns:
        str: Abstractive summary.
    """
    input_text = "summarize: " + text.strip().replace("\n", " ")
    input_ids = t5_tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    summary_ids = t5_model.generate(
        input_ids,
        max_length=max_length,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True
    )
    return t5_tokenizer.decode(summary_ids[0], skip_special_tokens=True)


def summarize_with_textrank(text: str, num_sentences: int = 3) -> str:
    """
    Extractive summarization using TextRank via sumy.

    Args:
        text (str): Raw input text.
        num_sentences (int): Number of summary sentences.

    Returns:
        str: Extractive summary.
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, num_sentences)

    return " ".join(str(sentence) for sentence in summary)


def summarize(text: str, method: Literal["t5", "textrank"] = "t5") -> str:
    """
    Wrapper function to switch summarization backend.

    Args:
        text (str): Text to summarize.
        method (str): 't5' for transformer or 'textrank' for extractive.

    Returns:
        str: Final summary string.
    """
    if len(text.strip().split()) < 30:
        return text.strip()  # Too short to summarize

    if method == "t5":
        return summarize_with_t5(text)
    elif method == "textrank":
        return summarize_with_textrank(text)
    else:
        raise ValueError("Invalid summarization method. Choose 't5' or 'textrank'.")
