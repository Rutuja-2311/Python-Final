#For loop

a = range(1, 11) #This will generate numbers from 1 to 10
for i in a:
    print(i)

for i in range(20, 51): #This will generate numbers from 20 to 50
    print(i)

for i in range(16 , 1): 
    print(i) #This will not print anything because the range is empty      

for i in range(16, 1, -1): #This will generate numbers from 16 to 2 in reverse order
    print(i)

for i in range(-5 , -16, -1): #This will generate numbers from -5 to -15 in reverse order
    print(i)

#Lets print a table of 5 using for loop

for i in range(5, 51, 5): #This will generate numbers from 5 to 50 with a step of 5
    print(i)

n = int(input("Enter a number to print its table: "))
for i in range(n, (n*11)+1, n): #This will generate numbers from n to n*10 with a step of n
    print(f"{n} x {i} = {n*i}")


#loops on strings
b = "Hello, World!"
for i in range(len(b)): #This will generate numbers from 0 to the length of the string - 1
   print(b[i]) #this will print each character of the string on a new line

c = "Hey, how are you?"
for i in c: #This will iterate over each character of the string
    print(i) #this will print each character of the string on a new line

#Break from loop
for i in range(1, 20): #This will generate numbers from 1 to 19
    if i == 10:
        break #This will break the loop when i is equal to 10
    else:
        print(i) #this will print numbers from 1 to 9

#Continue in loop
for i in range(1, 20): #This will generate numbers from 1 to 19
    if i == 10:
        continue #This will skip the rest of the loop when i is equal to 10
    else:
        print(i) #this will print numbers from 1 to 9

#Else in loop
for i in range(1, 20): #This will generate numbers from 1 to 19
    if i == 15:
        print("Break statement was executed") #this will be printed when i is equal to 10
        break #This will break the loop when i is equal to 10
    print(i) #this will print numbers from 1 to 9

else:
    print("Break statement was not executed") #this will not be printed because the loop was broken

#Quetions
#1. Accept an integer and Print hello world n times

n = int(input("Enter an integer: "))
for i in range(n):
    print("Hello, World!") #This will print "Hello, World!" n times

#2. Print natural number up to n

n = int(input("Enter an integer: "))
for i in range(1, n+1):
    print(i) #This will print natural numbers from 1 to n

#3. Reverse for loop. Print n to 1

n = int(input("Enter an integer: "))
for i in range(n, 0, -1):
    print(i) #This will print numbers from n to 1 in reverse order

#4. Take a number as input and print its table

n = int(input("Enter an integer: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}") #This will print the table of n from 1 to 10 

#5. Sum up to n terms

n = int(input("Enter an integer: "))
sum = 0
for i in range(1, n+1):
    sum += i #This will add each number from 1 to n to the sum
print(f"Sum of first {n} natural numbers is: {sum}") #This will print the sum of first n natural numbers

#6. Factorial of a number

n = int(input("Enter an integer: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i #This will multiply each number from 1 to n to the factorial
print(f"Factorial of {n} is: {factorial}") #This will print the factorial of n

#7. Print the sum of all even & odd numbers in a range separately

n = int(input("Enter an integer: "))
even_sum = 0
odd_sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"Sum of even numbers from 1 to {n} is: {even_sum}")
print(f"Sum of odd numbers from 1 to {n} is: {odd_sum}") #This will print the sum of even and odd numbers from 1 to n separately

#8. Print all the factors of a number

n = int(input("Enter an integer: "))

for i in range(1, n+1):
    if n % i == 0:
        print(i) #This will print all the factors of n

#9. Accept a number and check if it a perfect number or not. 
# A number whose sum of factors is equal to the number itself 
#Ex -  6 = 1, 2, 3 = 6

n = int(input("Enter an integer:"))
sum_of_factors = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_factors += i

if sum_of_factors == n:
    print(f"{n} is a perfect number") #This will print if n is a perfect number
else:
    print(f"{n} is not a perfect number") #This will print if n is not a perfect number

#10. Check wether the number is prime or not

n = int(input("Enter an integer: "))
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
    print(f"{n} is not a prime number") #This will print if n is not a prime number
if is_prime:
    print(f"{n} is a prime number") #This will print if n is a prime number
else:
    print(f"{n} is not a prime number") #This will print if n is not a prime number

#11. Reverse a string without using in build functions

n = input("Enter a string: ")
reversed_string = ""
for i in range(len(n)-1, -1, -1):
    reversed_string += n[i] #This will add each character of the string to the reversed_string in reverse order
print(f"Reversed string is: {reversed_string}") #This will print the reversed string

#12. Check string is Pallindrome or not

b = input("Enter a string: ")
reversed_string =""
for i in range(len(b)-1, -1, -1):
    reversed_string += b[i] #This will add each character of the string to the reversed_string in reverse order
    print(f"Reversed string is: {reversed_string}") #This will print the reversed string

if b == reversed_string:
    print(f"{b} is a palindrome") #This will print if n is a palindrome
else:
    print(f"{b} is not a palindrome") #This will print if n is not a palindrome

# 13. Count all letters, digits, and special symbols from a given string 
# Given: str1 = "P@#yn26at^&i5ve" 
# Expected Outcome: 
# Total counts of chars, digits, and symbols 
# Chars = 8 
# Digits = 3 
# Symbol = 4

a = "Hey, I am Rutuja"

char = 0
dig = 0
spchr = 0

for i in a:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        spchr += 1
print(f"Your digits are {dig}\n Your alphabate are {char}\n Your special characters are {spchr} ")