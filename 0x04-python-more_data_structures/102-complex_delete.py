#!/usr/bin/python3

def complex_delete(a_dict, value):
    for key in list(a_dict.keys()):
        if a_dict[key] == value:
            del a_dict[key]
    return a_dict
