#!/usr/bin/python3
"""Using NumPy to Multiply 2 Matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Input: 2 matrices to multiply
    Output: the result mutliplied matrix if valid
    """
    return np.matmul(m_a, m_b)
