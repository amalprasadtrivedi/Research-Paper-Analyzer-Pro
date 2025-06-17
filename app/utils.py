# utils.py

import os
import logging
import datetime
from typing import Tuple
from pathlib import Path

# Setup logging
def setup_logger(name: str = "app_logger", level: int = logging.INFO) -> logging.Logger:
    """
    Initializes and returns a logger instance.

    Args:
        name (str): Logger name.
        level (int): Logging level.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

# Initialize logger
logger = setup_logger()

def allowed_file(filename: str, allowed_extensions: Tuple[str] = ('.pdf',)) -> bool:
    """
    Check if the uploaded file has an allowed extension.

    Args:
        filename (str): The name of the file.
        allowed_extensions (Tuple[str]): Allowed file extensions.

    Returns:
        bool: True if file is allowed, False otherwise.
    """
    return filename.lower().endswith(allowed_extensions)

def format_similarity(score: float) -> str:
    """
    Formats similarity score as a percentage string.

    Args:
        score (float): Similarity score between 0 and 1.

    Returns:
        str: Formatted percentage string.
    """
    return f"{round(score * 100, 2)}%"

def format_filename(uploaded_file) -> str:
    """
    Formats a secure file name based on upload time.

    Args:
        uploaded_file: The uploaded file object.

    Returns:
        str: Unique file name.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    original_name = Path(uploaded_file.name).stem
    return f"{original_name}_{timestamp}.pdf"

def truncate_text(text: str, max_words: int = 50) -> str:
    """
    Truncates text to a fixed number of words with ellipsis.

    Args:
        text (str): Input string.
        max_words (int): Maximum number of words to keep.

    Returns:
        str: Truncated text.
    """
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + "..."
