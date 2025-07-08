#!/usr/bin/python3
'''
Module that lists all cities from the database hbtn_0e_4_usa.
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

    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
        )
    rows = cursor.fetchall()

    for id, name, state in rows:
        print("({}, '{}', '{}')".format(id, name, state))
    cursor.close()
    db.close()
