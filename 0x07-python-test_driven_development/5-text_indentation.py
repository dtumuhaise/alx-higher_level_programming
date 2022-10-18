#!/usr/bin/python3
"""
module defines a function that prints
a text with 2 new lines after each of
the characters ., ? and :.
"""


def text_indentation(text):
    """module to print text with 2 new lines

    Args:
        text: text

    Raises:
        TypeError: if text is not a string

    """

    if type(text) in (int, float):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
