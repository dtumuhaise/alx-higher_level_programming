#!/usr/bin/python3
"""
script that lists all states from database
hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    states = cur.fetchall()
    if states is not None:
        for row in states:
            print(("({}, '{}'").format(row[0], row[1]))
        cur.close()
        db.close()
