#!/usr/bin/env python3
"""try to create a class and child class with override methods"""


class Fish:
    """Parent class 1: Fish"""
    def swim(self):
        print("The fish is swimming")
    
    def habitat(self):
        print("The fish lives in water")

class Bird:
    """Parent class 2: Bird"""
    def fly(self):
        print("The bird is flying")
    
    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """child class: FlyingFish"""
    def fly(self):
        print("The flying fish is soaring!")
    
    def swim(self):
        print("The flying fish is swimming!")
    
    def habitat(self):
        print("The flying fish lives both in water and the sky!")

"""Create an instance of the FlyingFish class"""
flying_fish = FlyingFish()

flying_fish.fly() 
flying_fish.swim()
flying_fish.habitat()


print(FlyingFish.mro())
