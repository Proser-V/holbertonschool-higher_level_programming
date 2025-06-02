#!/usr/bin/python3

"""
Description : This module contain a function that returns an object
(Python data structure) represented by a JSON string.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function that returns an object (Python data structure)
    represented by a JSON string.
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
