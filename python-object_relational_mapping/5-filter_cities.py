#!/usr/bin/python3
"""script that takes in the name of a state as an
argument and lists all cities of that state"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) != 5:
        print("Usage: {} <mysql username> <mysql password> \
<database name> <state name>".format(argv[0]))
        exit(1)

    try:

        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )

        cur = db.cursor()
        cur.execute("""
                    SELECT cities.name
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC
                    """, (argv[4],))
        rows = cur.fetchall()
        cities = []
        for row in rows:
            if row[0] not in cities:
                cities.append(row[0])

        print(",".join(cities))

    except MySQLdb.Error as e:
        print("MySQL Error : {}".format(e))

        cur.close()
        db.close()
