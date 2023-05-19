#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    def square(y):
        return list(map(lambda x: x ** 2, y))
    return list(map(square, matrix))
