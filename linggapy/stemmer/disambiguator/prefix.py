class PrefixDisambiguator:
    @staticmethod
    def disambiguate_prefix_rules_1(word: str):
        """
        prefix

        ng- (ngaba, aba)
            (ngukus, kukus)
            (ngulgul, gulgul)
        """
        prefix_list = ["ng"]
        result = []
        for prefix in prefix_list:
            if word.startswith(prefix):
                result.append(word[len(prefix) :])
                result.append("k" + word[len(prefix) :])
                result.append("g" + word[len(prefix) :])
        return result

    @staticmethod
    def disambiguate_prefix_rules_2(word: str):
        """
        prefix

        ny- (ny+a,y,r,l -> cVERB) -> (nyarik -> carik)
                                    (ny)
            (ny -> jVERB, nyemak -> jemak)
            (ny -> sVERB, nyampat -> sampat)

        """
        prefix_list = ["ny"]
        result = []
        for prefix in prefix_list:
            if word.startswith(prefix):
                result.append(word[len(prefix) :])
                result.append("c" + word[len(prefix) :])
                result.append("j" + word[len(prefix) :])
                result.append("s" + word[len(prefix) :])
        return result

    @staticmethod
    def disambiguate_prefix_rules_3(word: str):
        """
        prefix

        n- (nuun -> tuun)
            (nuwegang -> duweg)
        """
        prefix_list = ["n"]
        result = []
        for prefix in prefix_list:
            if word.startswith(prefix):
                result.append(word[len(prefix) :])
                result.append("t" + word[len(prefix) :])
                result.append("d" + word[len(prefix) :])
        return result

    @staticmethod
    def disambiguate_prefix_rules_4(word: str):
        """
        prefix

        ma- (majalan -> jalan)
            (maca -> baca), ma -> b
            (maku -> paku), ma -> p

        """
        prefix_list = ["ma"]
        result = []
        for prefix in prefix_list:
            if word.startswith(prefix):
                result.append(word[len(prefix) :])
                result.append("b" + word[len(prefix) :])
                result.append("p" + word[len(prefix) :])
        return result

    @staticmethod
    def disambiguate_prefix_rules_5(word: str):
        """
        prefix

        a, ka, sa, pa, pi
        """
        prefix_list = ["a", "ka", "sa", "pa", "pi"]
        result = []
        for prefix in prefix_list:
            if word.startswith(prefix):
                result.append(word[len(prefix) :])
        return result
