Introduction
Ce document présente plusieurs concepts fondamentaux de Python, notamment la gestion des objets, la mutabilité, et l'identité des objets. À travers des exemples de code, nous allons explorer comment ces concepts fonctionnent.
Table des Matières
Types de Données
Identité des Objets
Mutabilité
Exemples de Code
Types de Données
Python prend en charge plusieurs types de données, y compris :
Entiers : Immutables et peuvent être affectés à des variables.
Listes : Mutables et peuvent être modifiées après leur création.
Tuples : Immutables et définis par des parenthèses.
Identité des Objets
L'identité d'un objet en Python peut être vérifiée à l'aide de la fonction id(). Deux objets peuvent avoir le même contenu mais être des objets distincts en mémoire.
Exemple :
python
a = (1, 2)
b = (1, 2)
print(a is b)  # False

Mutabilité
Les listes sont mutables, ce qui signifie que leur contenu peut être modifié sans créer un nouvel objet. Les tuples, en revanche, sont immuables.
Exemple :
python
l1 = [1, 2, 3]
l2 = l1
l1 += [4]
print(l1)  # Affiche [1, 2, 3, 4]
print(l2)  # Affiche [1, 2, 3] (l2 n'est pas modifié)

Exemples de Code
Exemple d'Incrémentation
python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # Affiche 1

Explication : Les entiers sont immuables, donc a reste inchangé.
Exemple d'Assignation
python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)  # Affiche [1, 2, 3]

Explication : La réassignation dans la fonction ne change pas l1.
Identité des Objets avec Tuples
python
a = (1)
b = (1)
print(a is b)  # True (car a et b sont tous deux l'entier 1)

a = (1, 2)
b = (1, 2)
print(a is b)  # False (car a et b sont deux tuples distincts)

Utilisation de id()
python
a = [1, 2, 3]
print(id(a))           # Identifiant initial
a += [4]
print(id(a))           # Identifiant après modification (restera le même)