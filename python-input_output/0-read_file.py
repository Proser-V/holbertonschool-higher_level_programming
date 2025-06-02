#!/usr/bin/python3

"""
Description : This module contain a function that reads a file
"""


def read_file(filename=""):
	"""
	This function reads a file
	"""
	with open(filename, "r", encoding="utf-8") as file:
		content = file.read()
		print(content, end="")
