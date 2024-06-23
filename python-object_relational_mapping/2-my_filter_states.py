#!/usr/bin/python3

"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Créer un curseur
    cur = db.cursor()

    # Utilisation de paramètres pour la requête pour éviter les injections SQL
    query = "SELECT * FROM states WHERE name LIKE BINARY \
        %s ORDER BY states.id ASC"
    cur.execute(query, (argv[4],))

    # Récupération des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cur.close()
    db.close()
