import re


class Rule5(object):
    def extract(self, word):
        # remove pi- from beginning of word
        if re.match(r"^pi", word):
            return re.sub(r"^pi", "", word)
