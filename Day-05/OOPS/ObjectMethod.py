# it works with objects data 
# it first parameter is always self which is a reference to the current instance of the class
# acces the instance variables and methods of the class using self

class ClassName:
    def method(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

object = ClassName() # creating an object of the class
object.method(10, 20) # calling the method and passing values to it

print(object.attribute1) # accessing the attribute1 of the object
print(object.attribute2) # accessing the attribute2 of the object