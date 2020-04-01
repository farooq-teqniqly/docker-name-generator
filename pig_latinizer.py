"""
A pig-latinzer
"""
def pig_latinize(word_list):
    """
        Pig-latinizes a list of words.

        Args:
            word_list: The list of words to pig-latinize.

        Returns:
            A generator containing the pig-latinized words.
    """
    for word in word_list:
        if word is None:
            continue

        if len(word.strip()) == 0:
            continue

        if word.lower()[0] in "aeiou":
            yield word + "ay"
        else:
            yield word[1:] + word[0] + "ay"
