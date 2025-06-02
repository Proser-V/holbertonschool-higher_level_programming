#!/usr/bin/python3

"""
Description : This module contain a function that returns the JSON
representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    This function that returns the JSON representation of an object.
    """
    json_string = json.dumps(my_obj)
    return json_string
