#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    INPUT: value
    OUTPUT: value if integer otherwise exception msg
    """

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as exp:
        print("Exception: {}".format(exp), file=sys.stderr)
        return False
