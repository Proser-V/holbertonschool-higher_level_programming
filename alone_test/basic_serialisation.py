#!/usr/bin/python3
import json

my_dict = {
    "id": 42,
    "username": "alpha",
    "is_admin": False,
    "last_login": "2025-06-02T10:45:00"
}
with open("user.json", "w") as file:
    data = json.dump(my_dict, file)

with open("user.json", "r") as file:
    data2 = json.load(file)

print (data2)
