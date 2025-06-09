#!/usr/bin/python3
"""
Description: A module where we get some ressources from HTTP requests.
Print the ressources titles and write the dictionaries in a CSV file.
"""


import requests
import json
import csv


def fetch_and_print_posts():
    """
    A function that sends a HTTP get request and prints the titles from
    dictionary recieved in response.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        for dict in data:
            print(dict['title'])


def fetch_and_save_posts():
    """
    A function that sends a HTTP get request and prints the content of the
    dictionary recieved in response in a CSV file, excludind userId.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        for dict in data:
            del dict["userId"]
        with open("posts.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
