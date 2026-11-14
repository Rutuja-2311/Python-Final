a = 12
if a > 10:
    print("I will do task A")
else:
    print("I will do task B")


money = int(input("Please provide me the money :- "))

if money == 10:
    print("I will have a choco bar ice cream")

elif money == 20:
    print("I will have a vanilla ice cream")

elif money == 30:
    print("I will have a strawberry ice cream")

else:
    print("I will have a mango dolly")


#Quetions
#1.  Accept two numbers and print the greatest between them

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 == num2:
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num2} is greater than {num1}")

#2. Accept the gender from the user as char and print the respective greeting message 
#Ex - Good Morning Sir (on the basis of gender)

gender = input("Enter your gender (M/F): ")

if gender == "M" or gender == "m":
    print("Good Morning Sir")
elif gender == "F" or gender == "f":
    print("Good Morning Ma'am")
else:
    print("Invalid gender")

#3. Accept an integer and check whether it is an even number or odd.

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

#4. Accept name and age from the user. Check if the user is a valid voter or not.
#Ex- “hello shery you are a valid voter”

name = input("Enter your name: ")
age = int(input("Enter your age: "))    

if age >= 18:
    print(f"Hello {name}, you are a valid voter")
else:
    print(f"Hello {name}, you are not a valid voter")

#5. Accept a year and check if it a leap year or not (google to find out what is a leap year)

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#6. take the input of temperature in celsius
# Below 0°C → "Freezing Cold 
# 0°C to 10°C → "Very Cold 
# 10°C to 20°C → "Cold 
# 20°C to 30°C → "Pleasant 
# 30°C to 40°C → "Hot 
# Above 40°C → "Very Hot "

temp = int(input("Enter the temperature: "))

if temp < 0:
    print("Freezing Cold")
elif 0 <= temp < 10:
    print("Very Cold")
elif 10 <= temp < 20:
    print("Cold")
elif 20 <= temp < 30:
    print("Pleasant")
elif 30 <= temp < 40:
    print("Hot")
else:
    print("Very Hot")