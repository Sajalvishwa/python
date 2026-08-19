# Encapsulation in Python
# Encapsulation means wrapping data and methods inside a class
# and controlling access to the data.

class Student:

    def __init__(self, name,age, marks):
        self.name = name          # Public variable
        self._age = age          # Protected variable
        self.__marks = marks      # Private variable


    # Getter method - used to get/read private data
    def get_marks(self):
        return self.__marks


    # Setter method - used to change/update private data
    def set_marks(self, marks):
        self.__marks = marks


# Creating an object
student = Student("Sajal", 90)

# Accessing public variable
print(student.name)

# Accessing private variable using getter
print(student.get_marks())

# Changing private variable using setter
student.set_marks(95)

# Printing updated marks
print(student.get_marks())