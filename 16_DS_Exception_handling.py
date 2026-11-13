# #Syntax Error: 
# print("Hello, World!" #syntaxError: unexpected EOF while parsing

# #indentation error:
# a = 10
# if a == 10:
# print("hello")  # IndentationError: expected an indented block

#Exception Handling:
# a = int(input("Enter a number: "))  # ValueError: invalid literal for int() with base 10: 'abc'
# print(10 / a)  # ZeroDivisionError: division by zero

# print("ok, I have done the division")  # This line will not be executed if an exception occurs above 

#Try and Except block:

a = int(input("Enter a number: "))

try:
    print(10 / a)

# except ZeroDivisionError:
#     print("You cannot divide by zero")

except Exception as err:
    print(f"sorry, there is an error: {err}")

else:
    print("No error occurred, division was successful.")

finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")

#Raise

age = int(input("Enter your age: "))

try: 
     
    if age < 18:
      raise ValueError("Sorry, you must be at least 18 years old to proceed.")

    else:
      print("You are eligible to proceed.")
except Exception as err:
    print(f"Sorry, there is an error: {err}")
    
#NameError

b = 10
try:
    print(b + c)  # NameError: name 'c' is not defined  

except NameError as err:
    print(f"Sorry, there is an error: {err}")

