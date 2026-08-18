# Single Inheritance
# One parent class and one child class

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()      # Parent class method
dog.bark()     # Child class method