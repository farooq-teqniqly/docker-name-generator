"""
    pig_latinizer tests
"""

import unittest
from  pig_latinizer import pig_latinize

class TestPigLatinizer(unittest.TestCase):
    def test_pig_latinize_when_word_starts_with_vowel_returns_expected_result(self):
        # Arrange
        words = ["apple", "egg"]

        # Act
        pig_latinized_words = list(pig_latinize(words))

        # Assert
        self.assertTrue("appleay" in pig_latinized_words)
        self.assertTrue("eggay" in pig_latinized_words)

    def test_pig_latinize_when_word_starts_with_consonant_returns_expected_result(self):
        # Arrange
        words = ["nix", "rotten"]

        # Act
        pig_latinized_words = list(pig_latinize(words))

        # Assert
        self.assertTrue("ixnay" in pig_latinized_words)
        self.assertTrue("ottenray" in pig_latinized_words)

    def test_pig_latinize_when_word_is_only_whitespace_ignores_it(self):
        # Arrange
        words = ["  "]
        
        # Act
        pig_latinized_words = list(pig_latinize(words))

        # Assert
        self.assertEqual(0, len(pig_latinized_words))

    def test_pig_latinize_when_word_is_None_ignores_it(self):
        # Arrange
        words = [None]
        
        # Act
        pig_latinized_words = list(pig_latinize(words))

        # Assert
        self.assertEqual(0, len(pig_latinized_words))

if __name__ == "__main__":
    unittest.main()