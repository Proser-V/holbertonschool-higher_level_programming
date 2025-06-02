#!/usr/bin/python3

import json
import os
import sys

if len(sys.argv) != 3:
    print("Usage: ./save_user_json.py <username> <score>")
    sys.exit(1)

filename = "score.json"
username = sys.argv[1]
score = sys.argv[2]
new_entry = {username: score}

try:
    score = int(score)
except ValueError:
    print("Score must be an integer.")
    sys.exit(1)

if not os.path.exists(filename) and os.path.getsize(filename) == 0:
    with open(filename, "w") as file:
        json.dump(new_entry, file)
else:
    with open(filename, "r") as file:
        data = json.load(file)
        data.update(new_entry)
    with open(filename, "w") as file:
        json.dump(data, file)
