#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    result = 0

    for i, arg in enumerate(args):
        result += int(arg)

    print("{}".format(result))
