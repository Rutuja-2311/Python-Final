#Map
a = [1, 2, 3, 4, 5]

result = map(lambda x : x * 2, a)

print(list(result))

#
a = [2, 4, 6, 8, 10]

def double(x):
    return x * 2

result = map(double, a)

print(list(result))

#Filter

def even(x):
    if x % 2 == 0:
       return True
    else:
        return False

a = [1,2,3,4,5,6,7,8,9]

result = filter(even, a)

print(list(result))

#Using Lambda func

def even(x):
    if x % 2 == 0:
       return True
    else:
        return False

a = [1,2,3,4,5,6,7,8,9]

result = filter(lambda x : True if x % 2 == 0 else False, a)

print(list(result))

