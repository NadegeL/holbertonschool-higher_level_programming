#!/usr/bin/python3


"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()

    query_part1 = "SELECT * FROM states WHERE name = "
    query_part2 = "'{}'".format(argv[4])
    query = query_part1 + query_part2

    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
