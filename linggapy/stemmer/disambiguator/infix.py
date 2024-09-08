class InfixDisambiguator:
    @staticmethod
    def disambiguate_infix_rules_1(word: str) -> list:
        """
        infix

        - `-in-` (sinurat -> surat)
        - `-um-` (rumaksa -> raksa)
        - `-el-` (telusuk -> tusuk)
        - `-er-` (gerigi -> gigi)
        """
        infix_list = ["in", "um", "el", "er"]
        result = []
        for infix in infix_list:
            if word.find(infix, 1, 3) != -1:
                result.append(word.replace(infix, ""))
        return result
