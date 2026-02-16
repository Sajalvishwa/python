#class are template for creating objects

#object is an instance of a class

#class syntax:
class ClassName:
    #class body
    pass

#creating an object of the class
obj = ClassName()
print(obj)


#example of a class with attributes and methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

#creating an object of the Person class
person1 = Person("Alice", 30)
person1.greet() #Hello, my name is Alice and I am 30 years old.

#creating another object of the Person class
person2 = Person("Bob", 25)
person2.greet() #Hello, my name is Bob and I am 25 years old.
