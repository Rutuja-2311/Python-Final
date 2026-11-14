#Explicit Type Conversion in Python
a = 32
a = str(a)
print(type(a)) #This will print <class 'str'> because the variable 'a' is converted from an integer to a string using the str() function.

b = 43
b = float(b)
print(type(b)) #This will print <class 'float'> because the variable 'b' is converted from an integer to a float using the float() function.

#c = "fdv"
#c = int(c) #This will raise a ValueError because the variable 'c' is a string that cannot be converted to an integer using the int() function.
#print(type(c)) #This line will not be executed due to the ValueError raised in the previous line.

d = 65
print(bool(d)) #This will print True because the variable 'd' is a non-zero integer, and when converted to a boolean using the bool() function, it evaluates to True.

e = "Hello"
print(bool(e)) #This will print True because the variable 'e' is a non-empty string, and when converted to a boolean using the bool() function, it evaluates to True.

f = 0
print(bool(f)) #This will print False because the variable 'f' is zero, and when converted to a boolean using the bool() function, it evaluates to False.

g = False #0, 0.0, " ",'', [], {}, None are all considered False in Python.
print(bool(g)) #This will print False because the variable 'g' is a boolean with a value of False.

#Implicit Type Conversion in Python
h = 54
print(54/2) #This will print 27.0 because the variable 'h' is an integer, and when divided by 2, it is implicitly converted to a float.