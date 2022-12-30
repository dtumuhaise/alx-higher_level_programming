#!/usr/bin/python3
"""
takes argument and displays all values in the states
table of db where name matches the argumen
"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE"
                " '{:s}' ORDER BY id ASC".format(sys.argv[4]))
    db = cur.fetchall()
    for i in db:
        if i[1] == sys.argv[4]:
            print(i)
    cur.close()
    db.close()
