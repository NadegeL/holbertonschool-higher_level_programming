Comment ouvrir un fichier en Python
Vous pouvez ouvrir un fichier en utilisant la fonction intégrée open().

python
Copier le code
file = open('example.txt', 'r')  # Mode 'r' pour lecture
Modes courants :

'r' : Lecture (read)
'w' : Écriture (write) – écrase le fichier s’il existe
'a' : Ajouter (append) – ajoute du texte à la fin
'b' : Mode binaire (ex. pour des fichiers non-textuels)
Comment écrire du texte dans un fichier
Pour écrire dans un fichier, ouvrez-le en mode écriture ('w' ou 'a'), puis utilisez write().

python
Copier le code
with open('example.txt', 'w') as file:
    file.write('Ceci est un texte dans le fichier.\n')
Comment lire tout le contenu d'un fichier
Pour lire tout le contenu d'un fichier, vous pouvez utiliser la méthode read().

python
Copier le code
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
Comment lire un fichier ligne par ligne
Utilisez une boucle for pour lire un fichier ligne par ligne.

python
Copier le code
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
Comment déplacer le curseur dans un fichier
Vous pouvez utiliser seek() pour déplacer le curseur à une position spécifique dans le fichier.

python
Copier le code
with open('example.txt', 'r') as file:
    file.seek(10)  # Déplace le curseur à la 10ème position
    content = file.read()  # Lire à partir de là
    print(content)
Comment s'assurer qu'un fichier est fermé après utilisation
L'utilisation du mot-clé with permet de garantir que le fichier est automatiquement fermé après usage, même en cas d'erreur.

python
Copier le code
with open('example.txt', 'r') as file:
    content = file.read()
# Pas besoin de file.close(), c'est fait automatiquement
Qu'est-ce que l'instruction with et comment l'utiliser
L'instruction with gère le contexte d’ouverture et de fermeture des fichiers ou d’autres ressources. Elle simplifie la gestion des fichiers, notamment pour les fermer proprement.

python
Copier le code
with open('example.txt', 'r') as file:
    # le fichier est ouvert ici
    content = file.read()
# ici, le fichier est déjà fermé
Qu'est-ce que JSON ?
JSON (JavaScript Object Notation) est un format standard pour échanger des données structurées. Il est très utilisé pour la communication entre un client et un serveur.

Exemple JSON :

json
Copier le code
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
Qu'est-ce que la sérialisation ?
La sérialisation consiste à convertir une structure de données Python (par exemple un dictionnaire ou une liste) en un format comme JSON pour le stocker ou l’envoyer sur le réseau.

Qu'est-ce que la désérialisation ?
La désérialisation est l'inverse de la sérialisation : cela consiste à prendre des données dans un format comme JSON et les convertir en une structure Python.

Comment convertir une structure de données Python en chaîne JSON
Utilisez la méthode json.dumps() pour sérialiser une structure Python (par exemple un dictionnaire) en chaîne JSON.

python
Copier le code
import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)
print(json_string)
Comment convertir une chaîne JSON en structure de données Python
Utilisez json.loads() pour désérialiser une chaîne JSON en une structure Python.

python
Copier le code
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data['name'])  # Output: John
Comment accéder aux paramètres de la ligne de commande dans un script Python
Pour accéder aux paramètres passés en ligne de commande à un script Python, utilisez le module sys.

python
Copier le code
import sys

print("Nombre de paramètres :", len(sys.argv))
print("Les paramètres sont :", sys.argv)
Exécution :

less
Copier le code
$ python3 script.py arg1 arg2
Nombre de paramètres : 3
Les paramètres sont : ['script.py', 'arg1', 'arg2']
Conclusion
Avec ces concepts, vous avez une solide compréhension de la gestion des fichiers, du format JSON, de la sérialisation, et de la manipulation des paramètres en ligne de commande en Python.