import io
import random
from itertools import islice


def __read_file(path, target_set):
    """
    Reads a file and appends each line to a list.

    Args:
        path: The path to the file to read.
        target_set: The set to append each line to.

    Returns:
        None
    """

    with io.open(path, "r", encoding="utf8") as f:
        try:
            for line in f:
                target_set.add(line.replace(" ", "").strip())
        except UnicodeDecodeError:
            pass


def load_files(names_file, nouns_file):
    """
    Loads a names and nouns file.

    Args:
        names_file: The path to the names file.
        nouns_file: The path to the nouns file.

    Returns:
        A two element tuple. The first element is a list containing the names. The second element is a list
        containing the nouns. The lengths of each list is limited to 1000 elements.
    """
    max_results_to_return = 1000
    names = set()
    nouns = set()

    __read_file(names_file, names)
    __read_file(nouns_file, nouns)

    return list(islice(names, max_results_to_return)), list(islice(nouns, max_results_to_return))


def generate_name(names_nouns_tuple):
    """
    Generates a Docker style name in the format 'name_noun'.

    Args:
        names_nouns_tuple: An two element tuple. The first element is a list containing the names. The second element is
        a list containing the nouns.
    Returns:
        A name in the format 'name_noun'.
    """
    names, nouns = names_nouns_tuple
    return f"{random.choice(names)}_{random.choice(nouns)}".lower()
