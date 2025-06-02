#!/usr/bin/python3

"""
Description: A module to learn to serialize and deserialize custom Python
objects using the pickle module.
"""

import json
import pickle


class CustomObject:
    """
    A custom python class.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                return pickle.dump(self, file)
        except Exception as e:
            print("Serialization failed: {}".format(e))

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print("Deserialization failed: {}".format(e))
