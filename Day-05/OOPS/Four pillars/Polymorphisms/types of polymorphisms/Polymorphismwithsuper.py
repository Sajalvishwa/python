#Child class parent ke method ko override kar sakti hai aur super() se parent method ko bhi call kar sakti hai.

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog = Dog()
dog.sound()