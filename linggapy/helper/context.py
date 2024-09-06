from ..rules import pengater_rules, pangiring_rules, seselan_rules


class Context:
    def __init__(self, word, dictionary) -> None:
        self.word = word
        self.dictionary = dictionary

    def process(self, word: str) -> str:
        word = self.remove_pangater(word)
        word = self.remove_pangiring(word)
        word = self.remove_seselan(word)
        return word

    def remove_pangater(self, word: str) -> str:
        if word in self.dictionary:
            return word
        else:
            pengater = pengater_rules.Pengater()
            for rule in pengater.rules:
                res = rule.extract(self.word)
                if res in self.dictionary:
                    return res
                else:
                    res = word
            return res

    def remove_pangiring(self, word: str) -> str:
        if word in self.dictionary:
            return word
        else:
            pangiring = pangiring_rules.Pangiring()
            for rule in pangiring.rules:
                res = rule.extract(self.word)
                if res in self.dictionary:
                    return res
            return res

    def remove_seselan(self, word: str) -> str:
        if word in self.dictionary:
            return word
        else:
            seselan = seselan_rules.Seselan()
            for rule in seselan.rules:
                res = rule.extract(self.word)
                if res in self.dictionary:
                    return res
            return res
