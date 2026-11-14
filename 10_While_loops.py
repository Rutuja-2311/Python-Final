# a = 1

# while a <= 30:
#     print(a)
#     a = a + 1

# #Quetions
# #1. Separate each digit of a number and print it on the new line

# a = int(input("Enter a number: "))

# while a > 0:
#     print(a % 10)
#     a = a // 10

# #2. Accept a number and print its reverse

# a = int(input("Enter a number: "))

# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(rev)

#3. Accept a number and check if it is a pallindromic number (If number and its reverse are equal)

a = int(input("Enter a number: "))

copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

if copy == rev:
    print("Pallindromic number")
else:
    print("Not a pallindromic number")

# Create a random number guessing game with python

import random

num = random.randint(1,11)

tries = 0

while True:
    guess = int(input("Guess Your number b/w 1 to 10: "))

    if num == guess:
        tries += 1
        print("You are rigt")

    elif num < guess:
        print("Go a little lower")
        tries += 1

    elif num > guess:
        print("Go a little higher")
        tries += 1

    else:
        tries += 1
        print("Sorry you are wrong")