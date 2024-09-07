from linggapy.stemmer import Stemmer


class TestStemmer:
    stemmer = Stemmer()

    def test_example(self):
        example: str = "kajemak"
        expected: str = "jemak"
        assert self.stemmer.stem(example) == expected
