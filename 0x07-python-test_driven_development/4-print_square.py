#!/usr/bin/python3
"""
print_square module.

Define print_square function
"""


def print_square(size):
    """Print a square with '#' followed by a newline.
    size (int): the dimensions of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("{}".format('#' * size))
        
