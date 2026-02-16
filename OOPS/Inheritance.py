# it is multi level inheritance........

class employee:
    starttime = "9am"
    endtime = "5pm"

class programmer(employee):
    def __init__(self, name, language):
        self.name = name
        self.language = language

class manager(programmer):
    def __init__(self, name, department):
        self.name = name
        self.department = department

prog1 = programmer("Alice", "Python")
print(f"Programmer: {prog1.name}, Language: {prog1.language}, Start Time: {prog1.starttime}, End Time: {prog1.endtime}")
mgr1 = manager("Bob", "Sales")
print(f"Manager: {mgr1.name}, Department: {mgr1.department}, Start Time: {mgr1.starttime}, End Time: {mgr1.endtime}")


#it is multiple inheritance...........

class teacher :
    def __init__(self , salary):
        self.salary = salary

    

class student :
    def __init__(self , grade ,fess):
        self.grade = grade
        self.fess = fess

class teaching_assistant(teacher , student):
    def __init__(self , name, salary ,fess, grade):
        self.name = name
        super().__init__(salary)
        student.__init__(self , grade, fess)

  
    def profit(cls):
     print(f"profit: {cls.salary - cls.fess}")
        
ta1 = teaching_assistant("Charlie", 30000, 5000, "A")
ta1.profit()
print(f"Teaching Assistant: {ta1.name}, Salary: {ta1.salary}, Grade: {ta1.grade}, Fees: {ta1.fess}")