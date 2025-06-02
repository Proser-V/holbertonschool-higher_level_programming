#!/usr/bin/python3

"""
Description : This module contain a function that creates an Object
from a “JSON file”.
"""

import json


def load_from_json_file(filename):
    """
    This function that creates an Object from a “JSON file”.
    """
    with open(filename, "r") as file:
        return json.load(file)

