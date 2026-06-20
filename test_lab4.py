import unittest
from lab4 import Sentence, SentenceManager

class TestSentenceManager(unittest.TestCase):

    def setUp(self):
        self.s1 = Sentence("Привіт світе!")
        self.s2 = Sentence("Код діє.")
        self.s3 = Sentence("Один два три.")
        
        self.sentences = [self.s1, self.s2, self.s3]

    def test_sort_sentences(self):
        expected_order = [self.s1, self.s2, self.s3]
        sorted_sentences = SentenceManager.sort_sentences(self.sentences)
        self.assertEqual(sorted_sentences, expected_order)

    def test_find_same_success(self):
        target = Sentence("  ПРИВІТ\tсвіте!  ")
        index = SentenceManager.find_same(self.sentences, target)
        self.assertEqual(index, 0)

    def test_find_same_not_found(self):
        target = Sentence("Зовсім інше речення.")
        index = SentenceManager.find_same(self.sentences, target)
        self.assertEqual(index, -1)

    def test_space_normalization(self):
        s = Sentence("Одне\t\t\tслово   тут.")
        self.assertEqual(s.raw, "Одне слово тут.")

if __name__ == '__main__':
    unittest.main()