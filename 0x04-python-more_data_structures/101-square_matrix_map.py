#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda sublist: list(map(lambda e: e ** 2, sublist)), matrix))
