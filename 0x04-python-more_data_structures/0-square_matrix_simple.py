#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix == [] or matrix == [[]]:
        return matrix
    else:
        sq_matrix = []
        for i in range(len(matrix)):
            sq_matrix.append(list(map(lambda x: x * x, matrix[i])))
        return sq_matrix
