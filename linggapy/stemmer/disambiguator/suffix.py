class SuffixDisambiguator:
    @staticmethod
    def disambiguate_suffix_rules_1(word: str):
        """
        suffix
        -e (dokare -> dokar)
        -ne (siapne -> siap)
        -nne (bajunne -> baju)
        """
        suffix_list = ["e", "ne", "nne"]
        result = []
        for suffix in suffix_list:
            if word.endswith(suffix):
                result.append(word[: -len(suffix)])
        return result

    @staticmethod
    def disambiguate_suffix_rules_2(word: str):
        """
        suffix

        -a (dokare -> dokar)
        -na (siapne -> siap)
        -ina (bajunne -> baju)
        """
        suffix_list = ["a", "na", "ina"]
        result = []
        for suffix in suffix_list:
            if word.endswith(suffix):
                result.append(word[: -len(suffix)])
        return result

    @staticmethod
    def disambiguate_suffix_rules_3(word: str):
        """
        suffix

        -n (bukun -> buku)
        -in (miluin -> milu)
        -an (panakan -> panak)
        -nin (belinin -> beli)
        -nan (gedenan -> gede)
        """
        suffix_list = ["n", "in", "an", "nin", "nan"]
        result = []
        for suffix in suffix_list:
            if word.endswith(suffix):
                result.append(word[: -len(suffix)])
        return result

    @staticmethod
    def disambiguate_suffix_rules_4(word: str):
        """
        suffix
        - `-ang` (jemakang -> jemak)
        - ing (jeroing -> jero)
        - nang (gedenang -> gede)
        - ning (purnamaning -> purnama)
        - yang (satuayang -> satua)
        """
        suffix_list = ["ang", "ing", "nang", "ning", "yang"]
        result = []
        for suffix in suffix_list:
            if word.endswith(suffix):
                result.append(word[: -len(suffix)])
        return result
