#!/usr/bin/python3
'''
Module that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time, write one
that is safe from MySQL injections!
'''

import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pwd,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states ORDER BY id ASC;")
    rows = cursor.fetchall()

    for id, name in rows:
        if name == state_name:
            print("({}, '{}')".format(id, name))
    cursor.close()
    db.close()
