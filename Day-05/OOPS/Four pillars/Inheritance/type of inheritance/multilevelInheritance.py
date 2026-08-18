# Multilevel Inheritance
# A class inherits from another child class

class Grandfather:

    def house(self):
        print("Grandfather has a house")


class Father(Grandfather):

    def car(self):
        print("Father has a car")


class Son(Father):

    def bike(self):
        print("Son has a bike")


son = Son()

son.house()    # From Grandfather
son.car()      # From Father
son.bike()     # Son's own method