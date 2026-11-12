a = {}
print(type(a))  # <class 'dict'>

b = {1:"hello", 2:43}
print(b)  # <class 'dict'>

c = {"Name": "John",} 
print(c) #Mutable: Dictionaries are mutable, meaning you can change, add, or remove key-value pairs after creation.

d = {"Name": "John", 5:76, "City": "New York", "Name": "Doe", 5:76}
print(d) #Duplicates: Keys must be unique, but you can have duplicates in values.
         #Orderd: Dictionary follows insertion order.
         #Heterogeneous: A dictionary can store different types of keys and values, like integers, strings, lists, or even another dictionary.

#Dic example and syntax
d = {"Name": "John", "Age": 30, "City": "New York", 5: 43, 23: "Hello", 3.14: "Pi", (1, 2): "Tuple Key"}

print(d["Age"])  # Accessing value using key

d["City"] = "Los Angeles"  # Modifying value using key
print(d)

d.update({"Country": "USA"})  # Adding new key-value pair
print(d)

del d[(1, 2)]  # Deleting key-value pair using key
print(d)

#Dictionary traversing
e = {"Name": "John", "Age": 30, "City": "New York"}

for i in e:      #1st method
    print(e[i])  # Iterating through keys

for i in e.values(): #2nd method
    print(i)

#Deep copy
a = [1,2,3,4,5]

b = a

b[0] = 100

print(a)  # [100, 2, 3, 4, 5]

#Shallow copy
a = [1,2,3,4,5]

b = a.copy()  # shallow copy: Creates a new list with the same elements as the original list, but changes to one list do not affect the other.

b[0] = 100

print(a)  

#In dic
f = {"Name": "John", "Age": 30, "City": "New York"}

f2 = f.copy()  # shallow copy: Creates a new dictionary with the same key-value pairs as the original dictionary, but changes to one dictionary do not affect the other.
f2 = f.get("Name")  # Accessing value using key
print(f2)
print(f.items())  # Returns a view object that displays a list of a dictionary's key-value tuple pairs.


#Quetions
#1.  Write a Python script to merge two Python dictionaries?

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2} #1st method

print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for i in dict2:  #2nd method
    dict1[i] = dict2[i]

print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#2. Write a Python program to sum all the values in a dictionary?

d = {'a': 100, 'b': 200, 'c': 300}
sum = 0

for i in d:
    sum += d[i]

print("Sum of all values:", sum)  # Output: Sum of all values: 600

#3. Count the frequency of each element

a = [1, 2, 3, 4, 5, 1, 2, 3, 1]

frequency = {}

for i in a:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)  # Output: {1: 3, 2: 2, 3: 2, 4: 1, 5: 1}

#4.  Write a Python program to combine two dictionary by adding values for common keys.

b = {'a': 100, 'b': 200, 'c':300}
c = {'a': 300, 'b': 200, 'd':400}

for i in c:
    if i in b:
        b[i] += c[i]
    else:
        b[i] = c[i]

print(b)  # Output: {'a': 400, 'b': 400, 'c': 300, 'd': 400}