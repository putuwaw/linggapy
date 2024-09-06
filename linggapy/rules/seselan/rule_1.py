class Rule1(object):
    def extract(self, word: str):
        if (
            word.find("in") != -1
            and word.find("in") != 0
            and word.find("in") != len(word) - 2
        ):
            return word.replace("in", "")
        return word
