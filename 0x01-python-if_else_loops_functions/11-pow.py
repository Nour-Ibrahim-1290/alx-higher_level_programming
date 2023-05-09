#!/usr/bin/python3

def pow(a, b):
    output = a
    for i in range(2, b+1):
        output *= a
    return output
