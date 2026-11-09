# def hello():
#     print("This is a hello function so I am doing hello")

# hello()

# Positional argument

def sum(a, b):
    print(f"The sum of your numbers is {a + b}")

sum(12, 54)
sum(34, 33)

# Keyword argument

def hello(name, age):
    print(f"Your name is {name} and your age is {age}")

hello(age = 19, name = "Rutuja")

# Default argument

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        # Uses default value "Guest"
greet("Bob")   # Uses "Bob"

# Pllindrome 

def palindrome(str):
    rev = ""

    for i in range(len(str)-1, -1, -1):
        rev = rev + str[i]

    if rev == str:
        print(f"{str} is a Palindrome")
    else:
        print(f"{str} is not a Palindrome")


palindrome("Naman")
palindrome("Cursor")

#

def me():
    return "This is me"

print(me())