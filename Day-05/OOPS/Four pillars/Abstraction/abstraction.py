# Abstraction in Python
# Abstraction means hiding implementation details
# and showing only the necessary information.

from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):

    # Abstract method
    # Child class must implement this method
    @abstractmethod
    def sound(self):
        pass


# Child class
class Dog(Animal):

    # Implementing abstract method
    def sound(self):
        print("Dog barks")


# Creating object of child class
dog = Dog()

# Calling method
dog.sound()