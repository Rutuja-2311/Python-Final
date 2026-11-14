a = 65
b = 27

print(a + b)  # Addition Ans is 92
print(a - b)  # Subtraction Ans is 38
print(a * b)  # Multiplication Ans is 1755
print(a / b)  # Division Ans is 0.8
print(a % b)  # Modulus Ans is 12
print(a ** b)  # Exponentiation Ans is 12^15
print(a // b)  # Floor Division Ans is 0

#Assignment Operators
c = 10
print(c)  # Ans is 10

#Compound Assignment Operators
d = 20
d = d + 20  # d += 20 Ans is 40
d = d + 40  # d += 40 Ans is 80
d = d + 60  # d += 60 Ans is 140
e = 40
e -= 10  # e -= 10 Ans is 30
e *= 2  # e *= 2 Ans is 60
e /= 3  # e /= 3 Ans is 20.0
e //= 2  # e //= 2 Ans is 10.0
e %= 3  # e %= 3 Ans is 1.0
e **= 2  # e **= 2 Ans is 1.0
print(d)

# Comparison Operators
f = 10
g = 20
print(f == g)  # Equal to Ans is False
print(f != g)  # Not equal to Ans is True
print(f < g)   # Less than Ans is True
print(f > g)   # Greater than Ans is False
print(f <= g)  # Less than or equal to Ans is True
print(f >= g)  # Greater than or equal to Ans is False
#print("A" > 45)  # Ans is False because string cannot be compared with integer

#Ascii Value
print(ord('A'))  # Ascii value of A is 65
print(ord('a'))  # Ascii value of a is 97
print(ord('0'))  # Ascii value of 0 is 48

# Logical Operators
h = True
i = False
print(h and i)  # there is true and false so the answer is False. In logical AND both the values should be True to get True as output
print(h or i)   # there is true and false so the answer is True. In logical OR if any one value is True then the output will be True
print(not h)    # there is true so the answer is False. In logical NOT if the value is True then the output will be False


#Questions
#Answer True and Fals
#1. Print(126 > 130)
print(126 > 130)  # Ans is False

#2. print((456 == 456) != (235 == 236))
print((456 == 456) != (235 == 236))  # Ans is True

#3. print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)  # Ans is True

#4. print(True and bool(0))
print(True and bool(0))  # Ans is False because bool(0) is False and True and False is False 
