from .disambiguator import Disambiguator
from ..utils import Cacher, Loader
from ..corrector import Corrector
from ..normalizer import Normalizer


class Stemmer:
    """
    Stemmer class that used to stem the Balinese text language.
    """

    def __init__(self):
        self.cache = Cacher()
        self.normalizer = Normalizer()
        self.corrector = Corrector()
        self.disambiguator = Disambiguator()
        self.loader = Loader()
        self.root_words = self.loader.load_root_words()

    def stem(
        self, text: str, normalize: bool = True, correct_spelling: bool = True
    ) -> str:
        """
        Stem the Balinese text language.
        """
        try:
            if normalize:
                text = self.normalizer.normalize(text)

            splitted_text = text.split(" ")

            result = []
            for word in splitted_text:
                if word in self.root_words:
                    result.append(word)
                    continue
                if correct_spelling:
                    word = self.corrector.correct_spelling(word)

                candidates = self.disambiguator.disambiguate(word)
                isFound = False
                for candidate in candidates:
                    if candidate in self.root_words:
                        result.append(candidate)
                        isFound = True
                        break

                if not isFound:
                    result.append(word)

            return " ".join(result)
        except Exception as e:
            print(f"Failed to stem text: {text}, error: {e}")
            return text
