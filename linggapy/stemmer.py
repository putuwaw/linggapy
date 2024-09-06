from .helper import context
from .helper import utils


class Stemmer:
    _exceptions: dict = {}

    def __init__(self) -> None:
        self._dictionary = utils.get_dictionary()

    def stem(self, word: str) -> str:
        word_list = utils.normalize(word).split(" ")
        result = []
        for w in word_list:
            if w in self._exceptions:
                result.append(self._exceptions[w])
            else:
                result.append(self.stem_word(w))
        return " ".join(result)

    def stem_word(self, word: str) -> str:
        """
        Stem word
        """
        ctx = context.Context(word, self._dictionary)
        return ctx.process(word)

    def add_exception(self, exception: dict) -> None:
        """
        Add exception word to stemmer
        """
        self._exceptions.update(exception)

    def set_exceptions(self, exceptions: dict) -> None:
        """
        Set exception words to stemmer
        """
        self._exceptions = exceptions

    def get_exceptions(self) -> dict:
        """
        Get exception words from stemmer
        """
        return self._exceptions


stemmer = Stemmer()
