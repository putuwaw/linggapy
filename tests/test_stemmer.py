from linggapy.stemmer import Stemmer
import csv


class TestStemmer:
    @classmethod
    def setup_class(cls):
        """Initialize Stemmer instance and load CSV data once for all tests."""
        cls.stemmer = Stemmer()
        cls.data = cls.load_data_from_csv("tests/test_data/test_case_linggapy.csv")

    @staticmethod
    def load_data_from_csv(file_path) -> list[tuple[str, str]]:
        """Load CSV data as a list of (word, stem) tuples."""
        data = []
        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append((row[0], row[1]))  # (word, stem)
        return data

    def test_stemming_example(self):
        """Test the stemming with word from the example."""
        word = "kajemak"
        expected = "jemak"
        assert self.stemmer.stem(word) == expected

    def test_stemming_accuracy(self):
        """Test that the stemming accuracy is at least 80%."""
        threshold = 0.80
        correct_count = 0
        total_count = len(self.data)

        for word, expected in self.data:
            result = self.stemmer.stem(word)
            if result == expected:
                correct_count += 1

        accuracy = correct_count / total_count
        assert (
            accuracy >= threshold
        ), f"Accuracy {accuracy:.2%} is below the threshold of {threshold:.2%}"
