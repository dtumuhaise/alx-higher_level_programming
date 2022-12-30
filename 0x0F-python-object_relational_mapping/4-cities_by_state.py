#!/usr/bin/python3
"""
lists all cities from the database
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM cities ORDER BY id ASC"
    )

    cities = cur.fetchall()

    if cities is not None:
        for row in cities:
            print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
        cur.close()
        db.close()
