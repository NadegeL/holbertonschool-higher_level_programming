1. Qu'est-ce qu'une Superclasse, Baseclass ou Parentclass ?
En POO, une superclasse (ou classe de base, classe parent) est une classe qui est héritée par une ou plusieurs autres classes. La classe parent fournit des attributs (variables) et des méthodes (fonctions) qui peuvent être réutilisées ou modifiées dans les sous-classes.

Exemple :

python
Copier le code
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic animal sound")
2. Qu'est-ce qu'une Sous-classe ?
Une sous-classe est une classe qui hérite d'une autre classe (la classe parent). La sous-classe peut utiliser les méthodes et attributs de la classe parent, ou les redéfinir pour changer le comportement.

Exemple :

python
Copier le code
class Dog(Animal):  # Dog hérite de Animal
    def make_sound(self):
        print("Bark")
3. Lister tous les Attributs et Méthodes d'une Classe ou Instance
Vous pouvez utiliser la fonction Python intégrée dir() pour lister tous les attributs et méthodes d'une classe ou d'une instance.

Exemple :

python
Copier le code
class MyClass:
    def __init__(self):
        self.x = 10

    def hello(self):
        print("Hello")

# Lister les attributs et méthodes de la classe
print(dir(MyClass))

# Lister les attributs et méthodes d'une instance
instance = MyClass()
print(dir(instance))
4. Quand une Instance Peut-elle Avoir de Nouveaux Attributs ?
Une instance peut avoir de nouveaux attributs à tout moment après sa création, en les assignant dynamiquement.

Exemple :

python
Copier le code
class Person:
    def __init__(self, name):
        self.name = name

person = Person("John")
# Ajout dynamique d'un nouvel attribut
person.age = 30
print(person.age)  # Output: 30
5. Comment Hériter d'une Classe en Python
Pour hériter d'une autre classe, vous placez le nom de la classe parent entre parenthèses après le nom de la classe que vous créez.

Exemple :

python
Copier le code
class Car:
    def drive(self):
        print("Driving a car")

class ElectricCar(Car):  # Héritage de Car
    def charge(self):
        print("Charging the car")
6. Définir une Classe avec Plusieurs Classes de Base
Python prend en charge l'héritage multiple, ce qui signifie qu'une classe peut hériter de plusieurs classes.

Exemple :

python
Copier le code
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):  # C hérite de A et B
    pass

c_instance = C()
c_instance.method_a()  # Hérité de A
c_instance.method_b()  # Hérité de B
7. Quelle est la Classe par Défaut que Toutes les Classes Héritent ?
En Python, toutes les classes héritent par défaut de la classe intégrée object, sauf si une autre classe est spécifiée. Cette classe fournit des fonctionnalités de base comme la méthode __str__() et __eq__().

Exemple :

python
Copier le code
class MyClass:  # Hérite implicitement de object
    pass
8. Redéfinir une Méthode ou Attribut Hérité d'une Classe de Base
Pour redéfinir (override) une méthode ou un attribut, vous définissez simplement une méthode ou un attribut avec le même nom dans la sous-classe.

Exemple :

python
Copier le code
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):  # Override de greet
        print("Hello from Child")
9. Quels Attributs ou Méthodes Sont Disponibles par Héritage aux Sous-classes ?
En général, tous les attributs et méthodes d'une classe parent sont hérités par la sous-classe, à l'exception des attributs privés (ceux commençant par __). Les méthodes privées ne sont pas directement accessibles.

Exemple :

python
Copier le code
class Parent:
    def __init__(self):
        self.public = "This is public"
        self.__private = "This is private"

class Child(Parent):
    pass

child = Child()
print(child.public)  # Accessible
# print(child.__private)  # Erreur : attribut privé
10. But de l'Héritage
Le but principal de l'héritage est la réutilisation du code. Vous pouvez définir une fonctionnalité commune dans une classe de base, puis l'étendre ou la personnaliser dans les sous-classes.

Réutilisation du code : Ne réécrivez pas le même code, utilisez plutôt l'héritage pour le partager entre plusieurs classes.
Hiérarchie des classes : Il permet d'organiser les classes en hiérarchie logique, où les sous-classes représentent des spécialisations des superclasses.
11. Qu'est-ce que isinstance, issubclass, type et super ?
isinstance(object, class) : Vérifie si un objet est une instance d'une classe ou de ses sous-classes.
Exemple :

python
Copier le code
print(isinstance(5, int))  # True
issubclass(subclass, class) : Vérifie si une classe est une sous-classe d'une autre.
Exemple :

python
Copier le code
class A:
    pass

class B(A):
    pass

print(issubclass(B, A))  # True
type(object) : Retourne la classe de l'objet.
Exemple :

python
Copier le code
print(type(5))  # <class 'int'>
super() : Permet d'accéder aux méthodes et attributs de la classe parente dans la sous-classe. C'est souvent utilisé pour appeler le constructeur de la classe parent.
Exemple :

python
Copier le code
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Appelle le constructeur du parent
        print("Child constructor")
