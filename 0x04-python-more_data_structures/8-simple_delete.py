#!/usr/bin/python3

def simple_delete(a_dict, key=""):
    if key in a_dict.keys():
        del a_dict[key]
    return a_dict
