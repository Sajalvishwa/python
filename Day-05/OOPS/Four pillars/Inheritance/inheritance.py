# Inheritance in Python
# Inheritance allows a child class to use
# properties and methods of a parent class.


# Parent class
class Animal:

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")


# Child class
# Dog inherits Animal
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


# Creating object of child class
dog = Dog()

# Calling inherited methods
dog.eat()
dog.sleep()

# Calling child's own method
dog.bark()