#!/usr/bin/python3
"""Define Function fo rMatrix Manipulation"""


def matrix_mul(m_a, m_b):

    # Check if m_a and m_b are in fact lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are in fact list of lists, new function
    if not list_of_lists(m_a):
        raise TypeError("m_a must be a list of lists")
    elif not list_of_lists(m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are empty like [] or [[]]
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # Check elements of m_a and m_b for being ints or floats, new func
    if not correct_elements(m_a):
        raise TypeError("m_a should contain only integers or floats")
    elif not correct_elements(m_b):
        raise TypeError("m_b should contain only integers or floats")

    # Check if both m_a and m_b are Rectangles, new func
    if not isrectangle(m_a):
        raise TypeError("each row of m_a must be of the same size")
    elif not isrectangle(m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b can't be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply the 2 Matrices and return 2D Result
    return multiply(m_a, m_b)


def multiply(m_a, m_b):
    # Initialize the resulting matrix
    m_c = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]

    return m_c


def list_of_lists(m):
    for inner in m:
        if not isinstance(inner, list):
            return False

    return True


def correct_elements(m):
    for inner in m:
        for elm in inner:
            if not isinstance(elm, (int, float)):
                return False

    return True


def isrectangle(m):
    length = len(m[0])
    for inner in m[1:]:
        if len(inner) != length:
            return False

    return True
