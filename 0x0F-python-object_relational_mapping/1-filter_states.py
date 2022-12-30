#!/usr/bin/python3
"""
lists all states with an name starting with N
from database
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT id, name\
                WHERE NAME LIKE 'N%'\
                FROM states ORDER BY id ASC")

    states = cur.fetchall()
    if states is not None:
        print("({}, '{}')".format(row[0], row[1]))
    cur.close()
    db.close
