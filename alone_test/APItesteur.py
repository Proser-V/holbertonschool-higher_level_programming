#!/bin/usr/python3

import requests

BASE = "http://127.0.0.1:5000/"

data = [
	{"likes": 90, "name": "La video de mon sbi", "views": 986887},
	{"likes": 45, "name": "La video de mon sbi 2", "views": 176434},
	{"likes": 878, "name": "La video de mon sbi 3", "views": 7986887},
]

for i in range(len(data)):
	response = requests.put(BASE + "video/" + str(i), json=data[i])
	print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2", json="video/2")
print(response.json())
