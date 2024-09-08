from ..utils import Cacher

import re
import unicodedata


class Normalizer:
    """
    Class for Normalizing text
    """

    def __init__(self):
        self.cache = Cacher()

    def normalize(self, text: str) -> str:
        """
        Normalizes a single text string.
        """
        if self.cache.has(text):
            return self.cache.get(text)
        else:
            try:
                raw_text = text
                text = text.lower()
                text = (
                    unicodedata.normalize("NFKD", text)
                    .encode("ASCII", "ignore")
                    .decode("utf-8")
                )
                text = re.sub(r"[^a-z0-9\s-]", "", text)
                text = re.sub(r"\s+", " ", text)
                text = text.strip()

                self.cache.set(raw_text, text)
                return text
            except Exception as e:
                print(f"Failed to normalize text: {text}, error: {e}")
                return text
