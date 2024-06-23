#!/usr/bin/python3


"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name = %s"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print

    cursor.close()
    db.close()
