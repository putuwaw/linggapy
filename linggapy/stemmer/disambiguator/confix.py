class ConfixDisambiguator:
    @staticmethod
    def disambiguate_confix_rules_1(word: str) -> list:
        """
        confix

        - `pa-an` (pasirepan -> sirep)
        - `ma-an` (majemakan -> jemak)
        - `ma-in` (maririhin -> ririh)
        - `ka-an` (kasugihan -> sugih)
        """
        confix_list = [("pa", "an"), ("ma", "an"), ("ma", "in"), ("ka", "an")]
        result = []
        for confix in confix_list:
            prefix = confix[0]
            suffix = confix[1]
            if word.startswith(prefix) and word.endswith(suffix):
                result.append(word[len(prefix) : -len(suffix)])
        return result
