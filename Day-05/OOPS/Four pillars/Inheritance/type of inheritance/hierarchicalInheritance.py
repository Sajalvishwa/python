# Hierarchical Inheritance
# Multiple child classes inherit from one parent class

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


class Cat(Animal):

    def meow(self):
        print("Cat is meowing")


dog = Dog()
cat = Cat()

dog.eat()      # Inherited from Animal
dog.bark()

cat.eat()      # Inherited from Animal
cat.meow()