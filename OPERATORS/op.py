# arithmetic operators = + - * / % ** //
print(2 + 3)  # addition
print(5 - 2)  # subtraction
print(4 * 3)  # multiplication
print(10 / 2) # division
print(10 % 3) # modulus
print(2 ** 3) # exponentiation
print(10 // 3) # floor division

# comparison operators = == != > < >= <=
print(5 == 5)  # equal to
print(5 != 3)  # not equal to
print(5 > 3)   # greater than
print(5 < 10)  # less than
print(5 >= 5)  # greater than or equal to
print(5 <= 10) # less than or equal to

# logical operators = and or not
print(True and False)  # logical AND
print(True or False)   # logical OR
print(not True)        # logical NOT

#operators precedence
print(2 + 3 * 4)  # multiplication has higher precedence than addition
print((2 + 3) * 4) # parentheses change the order of evaluation

#type conversion
print(int(3.14))  # converts float to int
print(float(5))   # converts int to float
print(str(123))   # converts int to string
print(bool(0))    # converts int to boolean (False)
print(bool(1))    # converts int to boolean (True)

#user input
name = input("Enter your name: ")
print(f"Hello, {name}!")
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

