Qu'est-ce que la POO (Programmation Orientée Objet) ?
La programmation orientée objet (POO) est un paradigme de programmation qui organise le code autour d'objets plutôt que de fonctions et de logique. Les objets représentent des entités du monde réel ou abstraites, ayant des attributs (données) et des méthodes (comportements).

"First-class everything" (tout est de première classe)
En Python, tout est un objet. Cela signifie que les fonctions, les classes, les nombres, les chaînes de caractères, etc., sont traités comme des objets et peuvent être passés comme arguments, stockés dans des variables, et manipulés dynamiquement.

Qu'est-ce qu'une classe ?
Une classe est un plan ou une structure permettant de créer des objets. Elle définit les attributs et les méthodes que les objets de ce type auront.

Qu'est-ce qu'un objet et une instance ?
Un objet est une instance spécifique d'une classe. C'est une représentation concrète d'une classe avec des valeurs assignées à ses attributs. Une instance est un terme souvent utilisé pour décrire un objet spécifique créé à partir d'une classe.

Quelle est la différence entre une classe et un objet ou une instance ?
Une classe est un modèle général, tandis qu'un objet ou une instance est une occurrence spécifique créée à partir de cette classe.

Qu'est-ce qu'un attribut ?
Un attribut est une variable définie dans une classe et accessible par ses instances. Les attributs stockent des données liées à une instance ou à la classe elle-même.

Qu'est-ce qu'un attribut public, protégé et privé ?
Public : accessible de l'extérieur de la classe.
Protégé : conventionnellement, préfixé d'un underscore (_), et destiné à être utilisé uniquement à l'intérieur de la classe ou des sous-classes.
Privé : préfixé de deux underscores (__), ce qui le rend inaccessible directement de l'extérieur de la classe, sauf par des méthodes spécifiques.
Qu'est-ce que self ?
**self** est un mot-clé qui fait référence à l'instance courante de la classe dans laquelle on travaille. Il est utilisé pour accéder aux attributs et méthodes de l'objet courant.

Qu'est-ce qu'une méthode ?
Une méthode est une fonction définie dans une classe qui agit sur les objets de cette classe. Les méthodes peuvent modifier les attributs d'un objet ou exécuter d'autres actions.

Qu'est-ce que la méthode spéciale init et comment l'utiliser ?
**__init__** est un constructeur en Python. Il est appelé automatiquement lors de la création d'un nouvel objet d'une classe pour initialiser les attributs de l'objet. Voici un exemple :

python
Copier le code
class Personne:
    def __init__(self, nom, âge):
        self.nom = nom
        self.âge = âge
Qu'est-ce que l'Abstraction des données, l'Encapsulation des données, et le Masquage de l'information ?
Abstraction : c'est le processus qui consiste à cacher les détails complexes et ne montrer que les fonctionnalités essentielles.
Encapsulation : c'est le fait de regrouper les données (attributs) et les méthodes qui opèrent sur ces données dans une seule unité (classe), en limitant l'accès à certaines parties de l'objet.
Masquage de l'information : c'est la capacité de cacher les détails internes d'un objet, souvent en utilisant des attributs privés ou protégés.
Qu'est-ce qu'une propriété ?
Une propriété en Python est un mécanisme qui permet de contrôler l'accès aux attributs via des méthodes tout en conservant l'apparence d'un accès direct. On utilise souvent le décorateur @property.

Quelle est la différence entre un attribut et une propriété en Python ?
Un attribut est une variable simple stockée dans une instance d'objet, tandis qu'une propriété est un attribut spécial qui a des méthodes associées pour contrôler son accès et sa modification.

Quelle est la façon Pythonic d'écrire des getters et setters en Python ?
En Python, au lieu d'utiliser explicitement des méthodes get et set, on utilise les propriétés avec le décorateur @property pour le getter, et @nom_attribut.setter pour le setter. Voici un exemple :

python
Copier le code
class Rectangle:
    def __init__(self, largeur):
        self._largeur = largeur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, valeur):
        if valeur > 0:
            self._largeur = valeur
Comment créer dynamiquement de nouveaux attributs pour des instances existantes ?
En Python, il est possible d'ajouter des attributs à une instance après sa création :

python
Copier le code
obj = MonObjet()
obj.nouvel_attribut = 10
Comment lier des attributs à des objets et des classes ?
Les attributs peuvent être liés à des objets spécifiques ou à la classe elle-même. Si un attribut est défini dans la méthode __init__, il est lié à l'instance. Si défini directement dans la classe, il sera partagé entre toutes les instances.

Qu'est-ce que le dict d'une classe ou d'une instance de classe et que contient-il ?
Le **__dict__** est un dictionnaire qui contient tous les attributs définis pour une instance ou une classe. Cela inclut les méthodes, variables, etc.

Comment Python trouve-t-il les attributs d'un objet ou d'une classe ?
Python recherche les attributs d'abord dans l'objet lui-même, puis dans sa classe, puis dans les classes parentes (si héritage).

Comment utiliser la fonction getattr ?
La fonction:
 **getattr(objet, "nom_attribut", valeur_par_défaut)** 
 permet de récupérer la valeur d'un attribut d'un objet si celui-ci existe, sinon elle retourne une valeur par défaut