from .confix import ConfixDisambiguator
from .infix import InfixDisambiguator
from .prefix import PrefixDisambiguator
from .suffix import SuffixDisambiguator


class Disambiguator:
    """
    Disambiguator class to disambiguate or remove affixes from a word
    """

    def __init__(self):
        self.suffix_rules = [
            SuffixDisambiguator.disambiguate_suffix_rules_1,
            SuffixDisambiguator.disambiguate_suffix_rules_2,
            SuffixDisambiguator.disambiguate_suffix_rules_3,
            SuffixDisambiguator.disambiguate_suffix_rules_4,
        ]
        self.prefix_rules = [
            PrefixDisambiguator.disambiguate_prefix_rules_1,
            PrefixDisambiguator.disambiguate_prefix_rules_2,
            PrefixDisambiguator.disambiguate_prefix_rules_3,
            PrefixDisambiguator.disambiguate_prefix_rules_4,
            PrefixDisambiguator.disambiguate_prefix_rules_5,
        ]
        self.infix_rules = [InfixDisambiguator.disambiguate_infix_rules_1]
        self.confix_rules = [ConfixDisambiguator.disambiguate_confix_rules_1]

    def disambiguate(self, word: str) -> set[str]:
        """
        Disambiguate word by (brute force) removing all possible affixes
        """
        result = []
        result.extend([word])
        for rule in self.suffix_rules:
            result.extend(rule(word))

        for s_word in result:
            for rule in self.prefix_rules:
                result.extend(rule(s_word))

        for p_word in result:
            for rule in self.infix_rules:
                result.extend(rule(p_word))

        for rule in self.infix_rules:
            result.extend(rule(word))

        for rule in self.confix_rules:
            result.extend(rule(word))
        return set(result)
