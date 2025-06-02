#!/usr/bin/python3

import pickle
import os
from datetime import datetime
import sys

if len(sys.argv) < 2:
    print("Usage: ./session.py <username>")
    sys.exit(1)

now = datetime.now().strftime("%Y-%m%d %H:%M:%S")
username = sys.argv[1]
new_entry = {username : now}
filename = "session.pkl"
my_log = {}

if not os.path.exists(filename) or os.path.getsize(filename) == 0:
    my_log.update(new_entry)
    print("Nouvelle session")
    with open(filename, "wb") as file:
        pickle.dump(my_log, file)
else:
    with open(filename, "rb") as file:
        my_log = pickle.load(file)

    my_log.update(new_entry)
    print("Session restaurée")

    with open(filename, "wb") as file:
        pickle.dump(my_log, file)
