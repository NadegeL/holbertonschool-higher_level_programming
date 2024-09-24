#!/usr/bin/env python3
"""creating an abstract class"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal class"""
    @abstractmethod
    def sound(self):
        """methode abstraite"""
        pass


class Dog(Animal):
    """Class herite de Animal"""

    def sound(self):
        """methode"""
        return "Bark"


class Cat(Animal):
    """class herite de Animal"""

    def sound(self):
        """methode"""
        return "Meow"
