#!/usr/bin/python3

def best_score(a_dict):
    if a_dict is None:
        return None

    max_val = max(a_dict.values())
    for key in a_dict.keys():
        if a_dict[key] == max_val:
            return key
