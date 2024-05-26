#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Defines the class
    """
    @abstractmethod
    def sound(self):
        """
    abstract method
        """
        pass


class Dog(Animal):
    """
    Dog class inherits from Animal
    """

    def sound(self):
        """
        Method that return the string Bark
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class inherits from Animal
    """

    def sound(self):
        """
        Method that return the string Meow
        """
        return "Meow"
