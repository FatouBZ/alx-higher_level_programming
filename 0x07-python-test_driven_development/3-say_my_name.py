#!/usr/bin/python3
"""
say_my_name module.

Define say_my_name function.
"""


def say_my_name(first_name, last_name=""):
    """Print "My name is " and two strings.
    first_name(str): the first string to print.
    last_name(str)(default=""): the second string to print.
    """
    if first_name is None:
        first_name = ""
    if last_name is None:
        last_name = ""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
       
