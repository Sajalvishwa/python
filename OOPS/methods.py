#methods= 1. Instance methods
#           2. Class methods
#           3. Static methods

#1. Instance methods = 1st parameter is always self
#                     can access and modify the instance attributes
#                     can access the class attributes   
class laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
laptop1 = laptop("Dell", "XPS 13")
laptop1.display_info() #Brand: Dell, Model: XPS 13

#2. Class methods = 1st parameter is always cls
#                   can access and modify the class attributes  
#                   cannot access the instance attributes
class laptop:
    brand = "Dell" #class attribute

    def __init__(self, model):
        self.model = model #instance attribute

    @classmethod
    def display_brand(cls):
        print(f"Brand: {cls.brand}")
laptop.display_brand() #Brand: Dell 
laptop1 = laptop("XPS 13")
laptop1.display_brand() #Brand: Dell

#3. Static methods = do not take self or cls as the first parameter
#                    cannot access or modify the instance attributes
#                    cannot access or modify the class attributes
class laptop:
    @staticmethod
    def display_message():
        print("This is a static method.")
laptop.display_message() #This is a static method.
laptop1 = laptop()
laptop1.display_message() #This is a static method.

