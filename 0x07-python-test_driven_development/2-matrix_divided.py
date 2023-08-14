#!/usr/bin/python3
"""
   matrix_divided module.

   Defines matrix_divided function.
"""


def matrix_divided(matrix, div):
    """Divide each element in a matrix by a divisor.
    matrix [[]]: a list of lists of float or int.
    div (int): non-zero integer divisor.

    Returns a new matrix.
    See tests/2-matrix_divided.txt for test cases.
    """
    if not isinstance(matrix, list) or\
       not any(isinstance(matrix[0], list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix " +
                    "(list of lists) of integers/floats")
    for row in matrix:
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
