#Ternary operations
a = 12

print("even") if a%2 == 0 else print("Odd")

#

# l = []
# for i in range(1, 21):
#     if i % 2 == 0 :
#         l.append(i)

# print(l)

#List Comphrehension

l = [i for i in range(1, 21) if i % 2 == 0]

print(l)

#Dictionary Comprehension

b = {i : i ** 2 for i in range(1, 10)}

print(b)

#Set comprehension

c = {i * 2 for i in range(10) if i % 2 == 0}

print(c)
