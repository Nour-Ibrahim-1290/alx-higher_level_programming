#!/usr/bin/python3

def uppercase(s):
    output = ""
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            output += chr(ord(s[i]) + (97 - 65))
        else:
            output += s[i]
    print(output)
