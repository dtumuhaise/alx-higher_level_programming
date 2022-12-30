#!/usr/bin/python3
"""
takes name of a state as argument and lists all cities
state in database
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":

    i = 0

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute(
        """SELECT cities.id, cities.name, states.name
         FROM cities
         LEFT JOIN states ON cities.state_id = states.id
         ORDER BY cities.id ASC"""
    )

    query_rows = cur.fetchall()

    for row in query_rows:
        if row[2] == argv[4]:
            if cont > 0:
                print(", ", end="")
            print(row[1], end="")
            i = i + 1
    print()
    cur.close()
    db.close()
