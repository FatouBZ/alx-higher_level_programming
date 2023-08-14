#!/usr/bin/python3
"""
text_indentation module.

Define text_indentation function.
"""


def text_indentation(text):
    """print a string with newlines after each '.' '?' and ':'.
    text (str): the string to parse and print.

    See tests/5-text_indentation.txt for test cases.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in ['.', '?', ':']:
        if c in text:
            text = text.replace(c, c + '\n\n\a')

    sen_list = text.split('\a')
    for sentence in sen_list:
        print(sentence.strip(' '), end="")
