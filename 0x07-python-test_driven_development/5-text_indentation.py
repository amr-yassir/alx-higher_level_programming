#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """prints a text with 2 new lines afte special characters"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i in ".?:":
        text = (i + "\n\n").join(
                [line.strip(" ") for line in text.split(i)])

    print(text, end="")


    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/5-text_indentation.txt")
