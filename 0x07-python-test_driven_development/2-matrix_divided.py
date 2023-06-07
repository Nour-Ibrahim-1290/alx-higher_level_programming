#!/usr/bin/python3
"""This Module contains a function that divides a matrix to a number"""


def matrix_divided(matrix, div):
    """Return a new matrix which is the result of dividing matrix by div"""

    # checks for div (non-number and 0 checks)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check that all items in matrix are lists
    if sum([not isinstance(item, list) for item in matrix]) != 0:
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    # check for length of every row
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # check for values inside each row
    for row in matrix:
        if sum([not isinstance(value, (int, float)) for value in row]) != 0:
            msg = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(msg)

    # Perform Divion operation (matrix / div)
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(round(value / div, 2))
        result.append(new_row)

    return result
