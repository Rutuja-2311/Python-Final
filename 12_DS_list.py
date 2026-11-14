#List

a = [12, 13, 14, 15, 16, 12, 12, 34.5, True, print()]

    #Mutable: Mutability refers to whether an object's value can be changed after creation. 
    # And List allows this.
    #Duplicates: we know data structures are used to store multiple values so duplicates means 
    # same value occuring multiple time. List allows this
    #Ordered:  List maintains ordered data structure maintains the sequence of elements as they 
    # were inserted. This means you can access elements using their position (index).
    #Heterogenous: List have heterogenous nature that means we can have multiple data types inside the list.

print(a[2]) #Indexing
print(a[ 0: 5])
print(a[-1]) #Negative indexing

#1st way using index

for i in range(len(a)):
    print(a[i])

#2nd way directly on values

for i in a:
    print(i)

#Questions
#1. Print positive and negative elements of an List?

l = [12, -13, 14, -15, 16, -12, 12, 34.5, -45.6]

for i in l:
    if i >= 0:
        print(f"positive element is {i}")
    else:
        print(f"negative element is {i}")

#2. Mean of List elements?

l = [12, 13, 14, 15, 16, 12, 12, 34.5]

sum = 0
for i in l:
    sum += i

print(sum / len(l))

#3. Find the greatest element and print its index too?

l = [12, 13, 14, 15, 16, 12, 12, 34.5]

greatest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > greatest:
        greatest = l[i]
        index = i

print(f"The greatest element is {greatest} and its index is {index}")

#4. Find the second greatest element?

l = [12, 13, 14, 15, 16, 12, 12, 34.5]
greatest = l[0]
second_greatest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > greatest:
        second_greatest = greatest
        greatest = l[i]
    elif l[i] > second_greatest and l[i] != greatest:
        second_greatest = l[i]
        index = i

print(f"The second greatest element is {second_greatest} and its index is {index}")

#5. Check if List is sorted or not.

l = [12, 13, 14, 15, 16, 12, 12, 34.5]

is_sorted = True

for i in range(len(l) - 1):
    if l[i] > l[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("The list is sorted.")
else:
    print("The list is not sorted.")
