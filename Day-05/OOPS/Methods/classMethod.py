#1st parameter is always "cls"
#access the class variables and methods of the class using cls
#decarator @classmethod is used to define a class method

class student:

    college = "ABC College" # class variable

    @classmethod
    def method(cls,name,cgpa): #class attributes are created using class method
        cls.name = name
        cls.cgpa = cgpa

object = student() # creating an object of the class
object.method("Alice", 8.5) # calling the class method and passing values to

print(object.name) # accessing the name of the object
print(object.cgpa) # accessing the cgpa of the object
print(object.college) # accessing the class variable by using the object
print(student.college) # accessing the class variable by using the class name