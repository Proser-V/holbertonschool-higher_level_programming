#!/usr/bin/python3
"""
Module Name: task_04_flyingfish.py

Description:
    This module include a class with multiple inheritence.
"""


class Fish:
    """
        A class Fish.
    """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
        A class Bird.
    """

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish:
    """
        A subclass with multiple inheritence.
    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
