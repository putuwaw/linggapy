import re


class Rule6(object):
    def extract(self, word):
        # remove a- from beginning of word
        if re.match(r"^a", word):
            return re.sub(r"^a", "", word)
