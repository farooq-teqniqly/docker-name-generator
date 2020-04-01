"""
    poor_mans_bar_chart tests
"""

import unittest
from poor_mans_bar_chart import render_chart


class TestPoorMansBarChart(unittest.TestCase):
    def test_render_chart_returns_expected_result(self):
        # Arrange
        word_list = ["apple", "pappy"]

        # Act
        chart = render_chart(word_list)

        # Assert
        self.assertEqual(2, len(chart["A"]))
        self.assertEqual(5, len(chart["P"]))
        self.assertEqual(1, len(chart["L"]))
        self.assertEqual(1, len(chart["E"]))
        self.assertEqual(1, len(chart["Y"]))

        zero_frequency_letters = [chr(n) for n in range(ord("A"), ord("Z") + 1) if chr(n) not in "APLEY"]

        for letter in zero_frequency_letters:
            self.assertEqual(0, len(chart[letter]))

    def test_render_ignores_symbols(self):
        # Arrange
        word_list = ["Hello", "world!"]

        # Act
        chart = render_chart(word_list)

        # Assert
        self.assertEqual(1, len(chart["H"]))
        self.assertEqual(1, len(chart["E"]))
        self.assertEqual(3, len(chart["L"]))
        self.assertEqual(2, len(chart["O"]))
        self.assertEqual(1, len(chart["W"]))
        self.assertEqual(1, len(chart["R"]))
        self.assertEqual(1, len(chart["D"]))

        zero_frequency_letters = [chr(n) for n in range(ord("A"), ord("Z") + 1) if chr(n) not in "HELOWRD"]

    def test_render_ignores_numbers(self):
        # Arrange
        word_list = ["Hello9", "1world!"]

        # Act
        chart = render_chart(word_list)

        # Assert
        self.assertEqual(1, len(chart["H"]))
        self.assertEqual(1, len(chart["E"]))
        self.assertEqual(3, len(chart["L"]))
        self.assertEqual(2, len(chart["O"]))
        self.assertEqual(1, len(chart["W"]))
        self.assertEqual(1, len(chart["R"]))
        self.assertEqual(1, len(chart["D"]))

        zero_frequency_letters = [chr(n) for n in range(ord("A"), ord("Z") + 1) if chr(n) not in "HELOWRD"]


if __name__ == "__main__":
    unittest.main()
