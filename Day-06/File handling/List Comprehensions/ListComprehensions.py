# ============================================================
#                    PYTHON LIST COMPREHENSION
# ============================================================


# ============================================================
# 1. BASIC LIST COMPREHENSION
# ============================================================

# Normal way:
numbers = []

for i in range(1, 6):
    numbers.append(i)

print("Normal List:", numbers)


# List Comprehension:
numbers = [i for i in range(1, 6)]

print("List Comprehension:", numbers)


# Syntax:
# [expression for item in iterable]


# ============================================================
# 2. SQUARE OF NUMBERS
# ============================================================

squares = [i ** 2 for i in range(1, 6)]

print("Squares:", squares)

# Output:
# [1, 4, 9, 16, 25]


# ============================================================
# 3. CUBE OF NUMBERS
# ============================================================

cubes = [i ** 3 for i in range(1, 6)]

print("Cubes:", cubes)


# ============================================================
# 4. EVEN NUMBERS
# ============================================================

even = [i for i in range(1, 11) if i % 2 == 0]

print("Even Numbers:", even)

# Syntax:
# [expression for item in iterable if condition]


# ============================================================
# 5. ODD NUMBERS
# ============================================================

odd = [i for i in range(1, 11) if i % 2 != 0]

print("Odd Numbers:", odd)


# ============================================================
# 6. EVEN NUMBERS KA SQUARE
# ============================================================

even_squares = [
    i ** 2
    for i in range(1, 11)
    if i % 2 == 0
]

print("Even Squares:", even_squares)

# Output:
# [4, 16, 36, 64, 100]


# ============================================================
# 7. LIST KE ELEMENTS KO DOUBLE KARNA
# ============================================================

numbers = [1, 2, 3, 4, 5]

double = [i * 2 for i in numbers]

print("Double:", double)

# Output:
# [2, 4, 6, 8, 10]


# ============================================================
# 8. LIST KE ELEMENTS KO SQUARE KARNA
# ============================================================

numbers = [2, 4, 6, 8]

squares = [i ** 2 for i in numbers]

print("Squares:", squares)

# Output:
# [4, 16, 36, 64]


# ============================================================
# 9. STRING WITH LIST COMPREHENSION
# ============================================================

word = "Python"

letters = [char for char in word]

print("Characters:", letters)

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']


# ============================================================
# 10. VOWELS FIND KARNA
# ============================================================

word = "python programming"

vowels = [
    char
    for char in word
    if char in "aeiou"
]

print("Vowels:", vowels)


# ============================================================
# 11. IF-ELSE WITH LIST COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

result = [
    "Even" if i % 2 == 0 else "Odd"
    for i in numbers
]

print("Result:", result)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# Syntax:
# [true_value if condition else false_value
#  for item in iterable]


# ============================================================
# 12. POSITIVE AND NEGATIVE NUMBERS
# ============================================================

numbers = [-5, -2, 0, 3, 7]

result = [
    "Positive" if i > 0
    else "Negative" if i < 0
    else "Zero"
    for i in numbers
]

print("Number Types:", result)


# ============================================================
# 13. NESTED LOOP
# ============================================================

result = [
    x
    for x in range(1, 4)
    for y in range(1, 3)
]

print("Nested Loop:", result)

# Output:
# [1, 1, 2, 2, 3, 3]


# ============================================================
# 14. CARTESIAN PRODUCT
# ============================================================

numbers = [1, 2, 3]
letters = ["A", "B"]

result = [
    (x, y)
    for x in numbers
    for y in letters
]

print("Cartesian Product:", result)

# Output:
# [(1, 'A'), (1, 'B'),
#  (2, 'A'), (2, 'B'),
#  (3, 'A'), (3, 'B')]


# ============================================================
# 15. NESTED LIST KO FLATTEN KARNA
# ============================================================

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

result = [
    num
    for row in matrix
    for num in row
]

print("Flattened List:", result)

# Output:
# [1, 2, 3, 4, 5, 6]


# ============================================================
# 16. FUNCTION WITH LIST COMPREHENSION
# ============================================================

def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]

result = [square(x) for x in numbers]

print("Function Result:", result)


# ============================================================
# 17. INPUT WITH LIST COMPREHENSION
# ============================================================

# User se multiple numbers input lena

# Example input:
# 10 20 30 40 50

# numbers = [int(x) for x in input("Enter numbers: ").split()]

# print("Numbers:", numbers)


# ============================================================
# 18. SET COMPREHENSION
# ============================================================

numbers = {i for i in range(1, 6)}

print("Set:", numbers)

# Syntax:
# {expression for item in iterable}


# ============================================================
# 19. DICTIONARY COMPREHENSION
# ============================================================

numbers = {
    i: i ** 2
    for i in range(1, 6)
}

print("Dictionary:", numbers)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ============================================================
# 20. IMPORTANT SYNTAX
# ============================================================

# Basic:
# [expression for item in iterable]


# With condition:
# [expression for item in iterable if condition]


# With if-else:
# [true_value if condition else false_value
#  for item in iterable]


# Nested loop:
# [expression
#  for item1 in iterable1
#  for item2 in iterable2]


# ============================================================
#                     QUICK REVISION
# ============================================================

# List Comprehension:
#
# [expression for item in iterable]
#
#
# Example:
#
# squares = [x ** 2 for x in range(1, 6)]
#
#
# With condition:
#
# even = [x for x in range(1, 11) if x % 2 == 0]
#
#
# With if-else:
#
# result = [
#     "Even" if x % 2 == 0 else "Odd"
#     for x in numbers
# ]
#
#
# Main Purpose:
# - Short code
# - List creation
# - Filtering
# - Transformation
# - Conditions
# - Nested loops