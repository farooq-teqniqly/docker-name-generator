"""
    A module that displays a poor-man's bar chart.
"""

def render_chart(word_list):
    """
        Renders a bar chart to the console. Each row of the chart contains the frequency
        of each letter in the word list.

        Returns:
            A dictionary whose keys are the letters and values are the freqency (N) of the
            letter. The value is a string containing the key repeated N times.

            For example in the string 'apple' the result would be like this:

            {"A": "a"},
            {"E": "e"},
            {"L": "l"},
            {"P": "pp"}

            Although not shown above all keys are returned even if the frequency is zero.

    """

    chart = {chr(n): "" for n in range(ord('A'), ord('Z') + 1)}

    for word in word_list:
        for letter in word:
            try:
                chart[letter.upper()] += letter.upper()
            except KeyError:
                continue
    return chart
