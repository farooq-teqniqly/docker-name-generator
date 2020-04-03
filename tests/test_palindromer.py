"""
    palindromer tests
"""

import unittest
from palindromer import load_words_from_url, find_palindromes, is_palingram, find_palingrams


class TestPoorMansBarChart(unittest.TestCase):
    def test_load_words_from_url_when_url_is_None_raises_ValueError(self):
        # Arrange, Act, Assert
        with self.assertRaises(ValueError):
            lines = list(load_words_from_url(None))

    def test_load_words_from_url_when_url_is_empty_raises_ValueError(self):
        # Arrange, Act, Assert
        with self.assertRaises(ValueError):
            lines = list(load_words_from_url(""))

    def test_load_words_from_url_when_url_invalid_raises_exception(self):
        # Arrange
        url = "http://greenteapress.com/thinkpython2/code/words.json"

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            lines = list(load_words_from_url(url))

    def test_load_words_returns_expected_result(self):
        # Arrange
        url = "http://greenteapress.com/thinkpython2/code/words.txt"

        # Act
        lines = list(load_words_from_url(url))

        # Assert
        self.assertEqual(113809, len(lines))

    def test_find_palindromes_returns_expected_result(self):
        # Arrange
        word_list = ["abba", "cat", "BbBb"]

        # Act
        palindromes = list(find_palindromes(word_list))

        # Assert
        self.assertTrue("abba" in palindromes)
        self.assertTrue("BbBb" in palindromes)
        self.assertTrue("cat" not in palindromes)

    def test_find_palindromes_when_word_list_is_None_raises_ValueError(self):
        # Arrange, Act, Assert
        with self.assertRaises(ValueError):
            palindromes = list(find_palindromes(None))

    def test_find_palindromes_when_word_list_is_empty_returns_empty_list(self):
        # Arrange, Act
        palindromes = list(find_palindromes([]))

        # Assert
        self.assertEqual(0, len(palindromes))

    def test_is_palingram_returns_true(self):
        # Arrange
        sentence = "Able was I ere I saw Elba."

        # Act, Assert
        self.assertTrue(is_palingram(sentence))

    def test_is_palingram_returns_false(self):
        # Arrange
        sentence = "This is not a palingram!"

        # Act, Assert
        self.assertFalse(is_palingram(sentence))

    def test_is_palingram_when_sentence_is_None_raises_ValueError(self):
        # Arrange, Act, Assert
        with self.assertRaises(ValueError):
            is_palingram(None)

    def test_is_palingram_when_sentence_is_empty_returns_false(self):
        # Arrange, Act, Assert
        self.assertFalse(is_palingram("  "))

    def test_find_palingrams_returns_expected_result(self):
        # Arrange
        # word_list = ["eroded", "dump", "ore", "legs", "sword", "mined", "mud"]
        word_list = ["fume", "emu"]

        # Act
        palingrams = list(find_palingrams(word_list))

        # Assert
        self.assertEqual(2, len(palingrams))
        self.assertTrue(("eroded", "ore") in palingrams)
        self.assertTrue(("dump", "mud") in palingrams)