#!/usr/bin/python3
"""
module defines a function that
divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    function to divide matrix elements and return new matrix

    Args:
        matrix: matrix
        div: number to divide the matrix with

    Raises:
        TypeError: matrix a list of lists of ints or floats
        TypeError: if Rows are not of same size
        TypeError: if div isn not float
        ZeroDivisonError: if Div = 0

    Returns:
        A new matrix
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[float("{:.2f}".format(j / div)) for j in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
