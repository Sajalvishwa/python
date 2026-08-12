# if , else , elif
age = int(input("Enter your age: "))
if age > 18:
    print("You are an adult")
elif age == 18:
    print("You are just an adult")
else:
    print("You are a minor")

# nested if
if age >= 18:
    if age < 60:
        print("You are an adult")
    else:
        print("You are a senior citizen")   
else:
    print("You are a minor")

# traffic light
color = input("Enter traffic light color (red, yellow, green): ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get ready")
elif color == "green":
    print("Go")
else:    print("Invalid color")

#multiple of 5 
number = int(input("Enter a number: "))
if number % 5 == 0:
    print(f"{number} is a multiple of 5")
else:    print(f"{number} is not a multiple of 5")      


#odd or even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:    print(f"{number} is odd")

