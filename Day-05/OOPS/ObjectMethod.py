# it works with objects data 
# it first parameter is always self which is a reference to the current instance of the class
# acces the instance variables and methods of the class using self

class student:

    college = "ABC College" # class variable


    def method(self,name,cgpa): #object attributes are created using method
        self.name = name
        self.cgpa = cgpa

object = student() # creating an object of the class
object.method("Alice", 8.5) # calling the method and passing values to it

print(object.name) # accessing the name of the object
print(object.cgpa) # accessing the cgpa of the object
print(object.college) # accessing the class variable by using the object
print(student.college) # accessing the class variable by using the class name