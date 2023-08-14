#!/usr/bin/python3
"""
   add_integer module.

   Defines add_integer function, safely.
"""


def add_integer(a, b=98):
    """Return the sum of a + b, both integers; b default is 98.
    a (int or float): if float, will be cast to int.
    b (int or float)(default = 98): if float, will be cast to int.

    See tests/0-add_integers.txt for test cases.
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
