# citation_extractor.py

import re
from typing import List

def extract_citations(text: str) -> List[str]:
    """
    Extracts potential citations or references from a research paper's text.

    Args:
        text (str): Full text of the research paper.

    Returns:
        List[str]: A list of detected citation strings.
    """
    # Normalize text and split by lines
    lines = text.splitlines()
    references = []
    in_references_section = False

    for line in lines:
        line = line.strip()

        # Detect start of references section
        if re.match(r"^(references|bibliography)\s*$", line.lower()):
            in_references_section = True
            continue

        if in_references_section:
            if line == "":
                continue

            # Detect citation line by simple regex or numbered format
            if re.match(r"^\[\d+\]", line) or re.match(r"^\d{1,3}\.\s", line):
                references.append(line)
            elif references and len(line.split()) > 3:
                # Continuation of previous line
                references[-1] += " " + line

    return references


def extract_inline_citations(text: str) -> List[str]:
    """
    Extracts inline citation markers like [1], [2-4], (Smith et al., 2020), etc.

    Args:
        text (str): Input research paper content.

    Returns:
        List[str]: List of inline citation strings.
    """
    citations = set()

    # Common inline citation patterns
    bracket_cites = re.findall(r"\[\d+(?:[-,]\d+)*\]", text)
    author_year_cites = re.findall(r"\([A-Z][a-z]+(?: et al\.)?,? \d{4}\)", text)

    citations.update(bracket_cites)
    citations.update(author_year_cites)

    return list(citations)
