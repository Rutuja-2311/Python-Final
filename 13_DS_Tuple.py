# a = (1,2,3,4,5)
# a[0] = 10

# print(a) #Immutable: Tuples are not mutable you cannot change the values of tuple.

# a = (1,2,3,4,5,5,3,4)
# print(a)   #Duplicates: You can have duplicate values in tuple there are no restriction.

# print(a[2]) #Ordered:  Set are ordered and you can access them through index values.

a = (1,2,3,4,5,5.5,print(), "Hello") #Heterogeneous: Set also have heterogenous nature and can have 
                                        #different types of data structure in tuple.

# for i in range(len(a)):
#     print(a[i]) #Indexing: You can access the elements of tuple using index values.

for i in a:
    print(i) #Iterable: You can iterate through the tuple using for loop.

indeces = a.index(5) #Indexing: You can find the index of an element in tuple using index() method.
print(indeces)

count = a.count(5) #Count: You can count the number of occurrences of an element in tuple using count() method.
print(count)

a,b,c,d = (1,2,3,4) #Unpacking: You can unpack the values of tuple into variables.
print(a)