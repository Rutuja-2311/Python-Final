s = {1, 2, 3, 4, 5} 
print(s) #mutable: Sets are mutable you can change the values of set.

s = {1, 2, 3, 4, 5, 5, 3, 4}
print(s) #Duplicates: You cannot have any duplicate values in sets that means every element will be unique.

# s = {1, 2, 3, 4, 5}
# print(s[1]) #Unorderd: Sets are unordered and you cannot access them through index values.

s = {1, 2, 3, 4, 5, 5.5, print(), "Hello"} 
print(s) #Heterogeneous: Set is semi-heterogenous it can store some data types like string, numbers, tuples but not everything.

#Hashing
a = hash("Hello") #Hashable: Set can store hashable data types like string, numbers, tuples but not everything.
print(a)

b = hash((1,3,432)) 
print(b)

#Set traversing
a  = {1, 2, 8, "Hello", 7, 9, 3, 4, 5}

for i in a:
    print(i) #Iterable: You can iterate through the set using for loop.

#Set methods
a = {1, 2, 3, 4, 5}

a.add(6) #Add: You can add an element to set using add() method.
print(a)

a.remove(2) #Remove: You can remove an element from set using remove() method.
print(a)

a.discard(3) #Discard: You can discard an element from set using discard() method.
print(a)

popped_element = a.pop() #Pop: You can remove and return an arbitrary element from set using pop() method.
print(popped_element)
print(a)

a.clear() #Clear: You can remove all elements from set using clear() method.
print(a)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

union_set = a.union(b) #Union: You can combine two sets using union() method.
print(union_set)

intersection_set = a.intersection(b) #Intersection: You can find the common elements between two sets using intersection() method.
print(intersection_set)

difference_set = a.difference(b) #Difference: You can find the elements that are in one set but not in the other using difference() method.
print(difference_set)

symmetric_difference_set = a.symmetric_difference(b) #Symmetric Difference: You can find the elements that are in either of the sets but not in both using symmetric_difference() method.
print(symmetric_difference_set)