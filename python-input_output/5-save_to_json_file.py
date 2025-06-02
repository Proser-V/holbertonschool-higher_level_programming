#!/usr/bin/python3

"""
Description : This module contain a function that
writes an Object to a text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function that writes an Object to a text file,
    using a JSON representation.
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
