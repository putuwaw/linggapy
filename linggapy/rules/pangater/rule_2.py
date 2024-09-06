import re


class Rule2(object):
    def extract(self, word):
        # remove ma- from beginning of word
        if re.match(r"^ma", word):
            return re.sub(r"^ma", "", word)
