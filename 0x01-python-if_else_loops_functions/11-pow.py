#!/usr/bin/python3

def pow(a, b):
    output = a
    if b >= 0:
        for i in range(2, b+1):
            output *= a
    else:
        for i in range(1, (-1 * b)+2):
            output /= a
    return output
