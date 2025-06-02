#!/usr/bin/python3

"""
Description: A module to gain experience in reading data from one format (CSV)
and converting it into another format (JSON) using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named 'data.json'.
    Returns True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False

    except Exception as e:
        return False
