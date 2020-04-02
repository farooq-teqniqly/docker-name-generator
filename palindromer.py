"""
    A module that finds palindromes.
"""

from urllib import request
from urllib.error import HTTPError
import io


def load_words_from_url(url):
    """
        Loads a dictionary file from the specified url. The remote content is expected
        to contain one word per line.

        Args:
            url: The dictionary file url.

        Returns:
            A generator containing the words in the dictionary file.

        Raises:
            ValueError: The dictionary url isn't specified.
            HTTPError: There was a problem downloading the dictionary file.
            IOError: There was a problem reading the downloaded dictionary file.
    """

    if url is None:
        raise ValueError("Specify the dictionary url.")

    try:
        file, _ = request.urlretrieve(url)
    except HTTPError as http_error:
        raise Exception(f"Unable to download file from {url}. HTTP status code: {http_error.code}. "
                        f"Error message: {http_error.msg}")

    with io.open(file, "r", encoding="utf8") as lines:
        try:
            for line in lines:
                yield line.strip()
        except IOError as io_error:
            raise Exception(f"Could not read downloaded file.", io_error)


def find_palindromes(word_list):
    """
        Finds palindromes in the specified word list.

        Args:
            word_list: A [list] of words.

        Returns:
            A generator containing the palindromes.

        Raises:
            ValueError: word_list is None.
    """
    if word_list is None:
        raise ValueError("Specify a [list] of words.")

    for word in word_list:
        if word.lower() == word[::-1].lower():
            yield word


def is_palingram(sentence):
    """
        Determines is the given sentence is a palingram.

        Args:
            sentence: The sentence to check.

        Returns:
            True if the sentence is a palingram, otherwise false.

        Raises:
            ValueError: No sentence was specified.
    """

    if sentence is None:
        raise ValueError("Specify a sentence to check.")

    if len(sentence.strip()) == 0:
        return False

    words = sentence.split(" ")
    normalized_sentence = ""

    for word in words:
        word = word.strip()
        if not word[-1].isalpha():
            word = word[:-1]

        normalized_sentence += word.lower()

    return normalized_sentence == normalized_sentence[::-1]
