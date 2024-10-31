Fonctions principales du curseur
Exécution de requêtes :
python
cursor.execute("SELECT * FROM table_name")

Récupération des résultats :
Récupérer une ligne :
python
row = cursor.fetchone()

Récupérer toutes les lignes :
python
rows = cursor.fetchall()

Récupérer un nombre spécifique de lignes :
python
rows = cursor.fetchmany(size=10)

Itération sur les résultats :
python
for row in cursor:
    print(row)

Exécution de requêtes avec paramètres :
python
cursor.execute("SELECT * FROM table_name WHERE id = %s", (some_id,))

Exécution de plusieurs requêtes :
python
cursor.executemany("INSERT INTO table_name (column1, column2) VALUES (%s, %s)", 
                   [("value1", "value2"), ("value3", "value4")])