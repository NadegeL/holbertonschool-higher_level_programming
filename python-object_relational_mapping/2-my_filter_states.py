#!/usr/bin/python3
"""lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    if len(argv) != 5:#vérification du nb d'argv
        print("Usage : {} username password database \
    state_name".format(argv[0]))
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
        # '%s' est un placeholder là ou on insert une valeur
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
                    ORDER BY states.id ASC", (argv[4],))
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQLdb Error: {}".format(e))

    finally:
        if 'cur' in locals():
            cur.close()

        if 'db' in locals():
            db.close()
