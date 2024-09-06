import re


class Rule1(object):
    def extract(self, word):
        pattern = r"^(.*?)(an)?$"
        match = re.match(pattern, word)
        if match:
            result = match.group(1)
            return result
        else:
            return word
