#!/usr/bin/python3
"""Function that writes an Object to a JSON file"""


import json


def save_to_json_file(my_obj, filename):
    """Accepts Python object and sends JSON representation to file"""

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
