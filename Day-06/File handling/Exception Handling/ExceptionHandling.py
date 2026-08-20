# ============================================================
#                 PYTHON EXCEPTION HANDLING
# ============================================================

# Exception Handling ka use program me aane wale errors ko
# handle karne ke liye hota hai, taaki program suddenly
# terminate na ho.
#
# Main Keywords:
# 1. try
# 2. except
# 3. else
# 4. finally
#
# Other Important:
# 5. raise
# 6. as
# ============================================================


# ============================================================
# 1. try
# ============================================================

# try block ke andar wo code likhte hain
# jisme exception/error aane ki possibility ho.

# Syntax:

# try:
#     risky code
#
# except:
#     error handle karne wala code


# ============================================================
# 2. except
# ============================================================

# Agar try block me exception aati hai,
# to except block execute hota hai.


# Example: FileNotFoundError
# ------------------------------------------------------------

try:

    # File ko read mode me open kar rahe hain
    with open("data.txt", "r") as file:

        # File ka data read karke print kar rahe hain
        print(file.read())

except FileNotFoundError:

    # Agar file exist nahi karti to ye execute hoga
    print("File not found")


# ============================================================
# 3. Multiple Exceptions
# ============================================================

# Ek try block ke saath multiple except blocks
# use kar sakte hain.


try:

    # User se number input le rahe hain
    num = int(input("Enter number: "))

    # Number ko 10 se divide kar rahe hain
    result = 10 / num

    print(result)


# Agar user number ki jagah text enter kare
# Example: hello
except ValueError:

    print("Please enter a number")


# Agar user 0 enter kare
# 10 / 0 possible nahi hai
except ZeroDivisionError:

    print("Cannot divide by zero")


# ============================================================
# 4. else
# ============================================================

# else block tab execute hota hai jab
# try block successfully execute ho jaye.
#
# Matlab:
# Exception aayi  -> except
# Exception nahi aayi -> else


try:

    a = 10
    b = 2

    print(a / b)


except ZeroDivisionError:

    print("Cannot divide by zero")


else:

    # Ye tab execute hoga jab try me
    # koi exception nahi aayegi
    print("Operation successful")


# ============================================================
# 5. finally
# ============================================================

# finally block HAMESHA execute hota hai.
#
# Exception aaye ya na aaye,
# finally execute hoga.


try:

    # Yaha ZeroDivisionError aayega
    print(10 / 0)


except ZeroDivisionError:

    print("Cannot divide by zero")


finally:

    # Exception aaye tab bhi execute hoga
    print("Program finished")


# ============================================================
# 6. Exception ko variable me store karna - "as"
# ============================================================

# "as e" ka use exception ki actual information
# ko variable me store karne ke liye hota hai.


try:

    print(10 / 0)


except ZeroDivisionError as e:

    # e ke andar error ki information store hogi
    print("Error:", e)


# Output:
# Error: division by zero


# ============================================================
# 7. General Exception
# ============================================================

# Exception ek general/base exception class hai.
#
# Isse hum different unexpected errors ko
# generally handle kar sakte hain.


try:

    result = 10 / 0

except Exception as e:

    print("Something went wrong:", e)


# Specific exception handle karna generally
# better practice hota hai.


# ============================================================
# 8. Common Exceptions
# ============================================================


# -------------------- ZeroDivisionError ---------------------

# Zero se divide karne par

# 10 / 0


# -------------------- ValueError ----------------------------

# Invalid value ko convert karne par

# int("hello")


# -------------------- TypeError -----------------------------

# Incompatible data types ke operation par

# 10 + "20"


# -------------------- IndexError ----------------------------

# List ke invalid index ko access karne par

# numbers = [10, 20, 30]
# print(numbers[5])


# -------------------- KeyError ------------------------------

# Dictionary ki non-existing key access karne par

# student = {"name": "Sajal"}
# print(student["age"])


# -------------------- FileNotFoundError ---------------------

# Non-existing file ko read mode me open karne par

# open("abc.txt", "r")


# ============================================================
# 9. raise Keyword
# ============================================================

# raise ka use manually exception generate karne
# ke liye hota hai.


age = 15

try:

    if age < 18:

        # Manually ValueError generate kar rahe hain
        raise ValueError("Age must be 18 or above")

except ValueError as e:

    print(e)


# ============================================================
# 10. Custom Exception
# ============================================================

# Hum apni khud ki exception class bhi bana sakte hain.
#
# Custom exception class ko generally Exception class
# se inherit karte hain.


class AgeError(Exception):

    # pass ka matlab abhi class ke andar
    # extra functionality nahi hai
    pass


age = 15

try:

    if age < 18:

        # Apni custom exception raise kar rahe hain
        raise AgeError("Age is less than 18")


except AgeError as e:

    print(e)


# ============================================================
# 11. Exception Handling with File
# ============================================================

# File handling ke saath exception handling
# bahut commonly use hoti hai.


try:

    with open("student.txt", "r") as file:

        print(file.read())


except FileNotFoundError:

    print("Student file not found")


# ============================================================
# 12. Complete Exception Handling Structure
# ============================================================

# Syntax:

# try:
#     # Risky code
#
# except SomeException:
#     # Error handle
#
# else:
#     # Jab exception nahi aaye
#
# finally:
#     # Hamesha execute hoga


# Complete Example:


try:

    num = int(input("Enter number: "))

    result = 100 / num


except ValueError:

    print("Please enter a valid number")


except ZeroDivisionError:

    print("Cannot divide by zero")


else:

    print("Result:", result)


finally:

    print("Execution completed")


# ============================================================
#                 EXCEPTION HANDLING FLOW
# ============================================================

#                    try
#                     |
#                     ↓
#              Exception aayi?
#                /          \
#              YES           NO
#               |             |
#               ↓             ↓
#            except         else
#               \             /
#                \           /
#                  ↓       ↓
#                   finally
#                      |
#                      ↓
#                     End


# ============================================================
# IMPORTANT POINTS
# ============================================================

# 1. try ke andar risky code likhte hain.

# 2. except exception ko handle karta hai.

# 3. Ek try ke saath multiple except ho sakte hain.

# 4. else tab execute hota hai jab exception nahi aati.

# 5. finally hamesha execute hota hai.

# 6. "as e" se exception ki information access kar sakte hain.

# 7. raise se manually exception generate kar sakte hain.

# 8. Custom exceptions Exception class se banayi ja sakti hain.

# 9. Specific exception handle karna generally better hai:
#
#    except ValueError:
#
#    instead of:
#
#    except Exception:


# ============================================================
# QUICK REVISION
# ============================================================

# try     -> Risky code
# except  -> Error handle
# else    -> No error
# finally -> Always execute
# raise   -> Manually error generate
# as e    -> Error ki information store


# ============================================================
# GOLDEN STRUCTURE
# ============================================================

# try:
#     risky_code
#
# except SpecificException:
#     handle_error
#
# else:
#     success_code
#
# finally:
#     always_execute