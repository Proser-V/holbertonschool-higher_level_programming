#!/usr/bin/python3

import csv
import os
import sys

if len(sys.argv) != 3:
    print("Usage: ./save_user_csv.py <username> <score>")
    sys.exit(1)

filename = "score.csv"
username = sys.argv[1]
score = sys.argv[2]
first_line = "username, score"
users = []
found = False

try:
    score = int(score)
except ValueError:
    print("Score must be an integer.")
    sys.exit(1)

score = str(score)
new_entry = {"username": username ,"score": score}

if os.path.exists(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)

for user in users:
    if user["username"] == username:
        user["score"] = score
        found = True
        break

if not found:
    users.append(new_entry)

with open(filename, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["username", "score"])
    writer.writeheader()
    writer.writerows(users)
