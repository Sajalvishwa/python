# a static method is a method that belongs to the class rather than an instance of the class. It does not require an instance of the class to be called and does not have access to the instance (self) or class (cls) variables. Static methods are defined using the @staticmethod decorator.


class calculator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y


obj = calculator() # creating an object of the class
print(obj.add(10, 5)) # calling the static method add
print(obj.subtract(10, 5)) # calling the static method subtract
print(obj.multiply(10, 5)) # calling the static method multiply
print(obj.divide(10, 5)) # calling the static method divide
