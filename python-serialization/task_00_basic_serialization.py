#!/usr/bin/python3

"""
Description: A module that adds the functionality to serialize a Python dictionary to a
JSON file and deserialize the JSON file to recreate the Python Dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    A function that serialize a Python dictionary to a JSON file.
    """
    json_output = json.dumps(data)
    with open(filename, "w")as file:
        return file.write(json_output)


def load_and_deserialize(filename):
    """
    A function that deserialize the JSON file to recreate the Dictionary.
    """
    with open(filename, "r") as file:
        return json.load(file)
