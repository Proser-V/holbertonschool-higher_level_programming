#!/usr/bin/python3

"""
Description : This module contain a function that returns an object
(Python data structure) represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    This function that returns an object (Python data structure)
    represented by a JSON string.
    """
    json_string = json.loads(my_str)
    return json_string
