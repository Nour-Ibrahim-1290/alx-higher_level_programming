#!/usr/bin/python3
"""Function that returns a string as a JSON"""

import json


def from_json_string(my_str):
    """Transform a string to JSON file
    Return: Python objects
    """
    return json.loads(my_str)
