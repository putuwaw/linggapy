import re


class Rule4(object):
    def extract(self, word):
        # remove pa- from beginning of word
        if re.match(r"^pa", word):
            return re.sub(r"^pa", "", word)
