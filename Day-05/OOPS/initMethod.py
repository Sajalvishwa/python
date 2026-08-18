# it is a method which is used to initialize the attributes of the class. 
# It is called automatically when an object of the class is created.
#  It is also known as a constructor. 

# syntax of init method
class ClassName:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

object = ClassName(10, 20) 

print(object.attribute1)
 # creating an object of the class and passing values to the init method

print(object.attribute2)
