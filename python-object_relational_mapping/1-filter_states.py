#!/usr/bin/python3
'''
Module that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa.
'''

import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

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
        if name[0] == "N":
            print("({}, '{}')".format(id, name))
    cursor.close()
    db.close()
