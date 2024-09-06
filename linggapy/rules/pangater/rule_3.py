import re


class Rule3(object):
    def extract(self, word):
        # remove sa- from beginning of word
        if re.match(r"^sa", word):
            return re.sub(r"^sa", "", word)
