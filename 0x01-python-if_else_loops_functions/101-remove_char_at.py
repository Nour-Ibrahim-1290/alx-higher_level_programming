#!/usr/bin/python3

def remove_char_at(s, n):
    output = ""
    for i in range(len(s)):
        if i == n:
            continue
        output += s[i]
    return output
