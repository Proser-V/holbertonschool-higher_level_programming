#!/bin/usr/python3

import requests

BASE = "http://127.0.0.1:5000/"

response = requests.patch(BASE + "video/2", json={"likes": 66666, "views": 222333})
print(response.json())
