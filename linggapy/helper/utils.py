import re
from os.path import dirname, join


def get_dictionary() -> set:
    base_dir = dirname(dirname(__file__))
    path = join(base_dir, "data", "kruna-lingga.txt")
    with open(path) as f:
        words = f.read().splitlines()
        words.sort(key=len, reverse=True)
        words_set = set(words)
    return words_set


def normalize(text: str) -> str:
    """
    Normalize text by removing unnecessary characters
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9 -]", "", text)
    text = re.sub(r"\b\d+\b", "", text)
    text = re.sub(r" +", " ", text)
    text = text.strip()
    return text
