import re


class Rule1(object):
    def extract(self, word):
        # remove ka- from beginning of word
        if re.match(r"^ka", word):
            return re.sub(r"^ka", "", word)
