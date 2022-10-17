#!/usr/bin/python3
"""
module defines a function that 
divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    function to divide matrix elements and return new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[float("{:.2f}".format(j / div)) for j in row] for row in matrix]


