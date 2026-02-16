#function = block of code which only runs when it is called

#syntax
def function_name():
    print("This is a function")

def add(a, b):
    return a + b #function with parameters and return value

function_name() #calling the function

#types of function
#1. built-in function
print("Hello, World!") #print is a built-in function
input("Enter your name: ") #input is a built-in function
type(123) #type is a built-in function
range(5) #range is a built-in function

#2. user-defined function
def greet(name):
    print(f"Hello, {name}!")

#lamda function = anonymous function
square = lambda a,b: a * b #lambda function to calculate the product of two numbers
print(square(5, 3)) #calling the lambda function

#factorial of a number
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")



