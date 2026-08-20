# ============================================================
#                    PYTHON JSON MODULE
# ============================================================

# JSON = JavaScript Object Notation
#
# JSON ka use data ko store aur exchange karne ke liye hota hai.
#
# Python me JSON ke saath kaam karne ke liye
# built-in "json" module use hota hai.

import json


# ============================================================
# 1. PYTHON DICTIONARY
# ============================================================

student = {
    "name": "Sajal",
    "age": 21,
    "course": "CSE",
    "skills": ["Python", "C++", "SQL"],
    "active": True
}

print("Python Dictionary:")
print(student)


# ============================================================
# 2. json.dumps()
# ============================================================

# dumps() Python object ko JSON STRING me convert karta hai.
#
# Python → JSON String

json_data = json.dumps(student)

print("\nJSON String:")
print(json_data)

print("\nType:")
print(type(json_data))


# ============================================================
# 3. json.dumps() WITH INDENT
# ============================================================

# indent ka use JSON ko readable/pretty format me
# display karne ke liye hota hai.

pretty_json = json.dumps(student, indent=4)

print("\nPretty JSON:")
print(pretty_json)


# ============================================================
# 4. sort_keys
# ============================================================

# sort_keys=True JSON ke keys ko alphabetically sort karta hai.

sorted_json = json.dumps(
    student,
    indent=4,
    sort_keys=True
)

print("\nSorted JSON:")
print(sorted_json)


# ============================================================
# 5. json.loads()
# ============================================================

# loads() JSON STRING ko Python object me convert karta hai.
#
# JSON String → Python Object

json_string = '{"name": "Sajal", "age": 21, "course": "CSE"}'

student_data = json.loads(json_string)

print("\nPython Object:")
print(student_data)

print("\nType:")
print(type(student_data))


# ============================================================
# 6. JSON DATA ACCESS
# ============================================================

print("\nStudent Name:")
print(student["name"])

print("\nStudent Age:")
print(student["age"])

print("\nStudent Skills:")
print(student["skills"])


# ============================================================
# 7. json.dump()
# ============================================================

# dump() Python object ko directly JSON FILE me write karta hai.
#
# Python Object → JSON File

with open("student.json", "w") as file:

    json.dump(
        student,
        file,
        indent=4
    )

print("\nStudent data saved to student.json")


# ============================================================
# 8. json.load()
# ============================================================

# load() JSON FILE se data read karke
# Python object me convert karta hai.
#
# JSON File → Python Object

with open("student.json", "r") as file:

    data = json.load(file)

print("\nData read from JSON file:")
print(data)


# ============================================================
# 9. JSON DATA UPDATE
# ============================================================

# JSON se data Python dictionary me load karne ke baad
# hum usko modify kar sakte hain.

data["age"] = 22
data["course"] = "Computer Science"

print("\nUpdated Data:")
print(data)


# Updated data ko wapas JSON file me save karna

with open("student.json", "w") as file:

    json.dump(
        data,
        file,
        indent=4
    )

print("\nUpdated data saved.")


# ============================================================
# 10. JSON LIST
# ============================================================

students = [
    {
        "name": "Sajal",
        "age": 21
    },
    {
        "name": "Rahul",
        "age": 20
    },
    {
        "name": "Aman",
        "age": 22
    }
]

print("\nStudents List:")
print(students)


# List ko JSON string me convert karna

students_json = json.dumps(
    students,
    indent=4
)

print("\nStudents JSON:")
print(students_json)


# ============================================================
# 11. JSON LIST KO FILE ME SAVE KARNA
# ============================================================

with open("students.json", "w") as file:

    json.dump(
        students,
        file,
        indent=4
    )

print("\nStudents saved to students.json")


# ============================================================
# 12. JSON FILE ME NEW STUDENT ADD KARNA
# ============================================================

# Pehle existing JSON file ko read karenge.

with open("students.json", "r") as file:

    students_data = json.load(file)


# New student

new_student = {
    "name": "Rohit",
    "age": 21
}


# List me new student add karna

students_data.append(new_student)


# Updated list ko file me save karna

with open("students.json", "w") as file:

    json.dump(
        students_data,
        file,
        indent=4
    )

print("\nNew student added.")


# ============================================================
# 13. JSON EXCEPTION HANDLING
# ============================================================

# Agar JSON ka format invalid hai,
# JSONDecodeError aa sakta hai.

invalid_json = '{"name": "Sajal", age: 21}'


try:

    data = json.loads(invalid_json)

    print(data)


except json.JSONDecodeError:

    print("\nInvalid JSON format!")


# ============================================================
# 14. EXCEPTION WITH JSON FILE
# ============================================================

try:

    with open("unknown.json", "r") as file:

        data = json.load(file)

        print(data)


except FileNotFoundError:

    print("\nJSON file not found.")


except json.JSONDecodeError:

    print("\nInvalid JSON data.")


# ============================================================
# 15. IMPORTANT JSON FUNCTIONS
# ============================================================

# json.dumps()
# Python Object → JSON String


# json.loads()
# JSON String → Python Object


# json.dump()
# Python Object → JSON File


# json.load()
# JSON File → Python Object


# ============================================================
# QUICK REVISION
# ============================================================

#                 JSON MODULE
#
#                     |
#          ┌──────────┴──────────┐
#          ↓                     ↓
#       STRING                  FILE
#          |                     |
#      dumps()                 dump()
#          ↓                     ↓
#       JSON                  JSON File
#          ↑                     ↑
#      loads()                 load()
#          |                     |
#       Python                Python
#
#
# Golden Trick:
#
# "s" = String
#
# dumps  → Python → JSON String
# loads  → JSON String → Python
#
# dump   → Python → JSON File
# load   → JSON File → Python