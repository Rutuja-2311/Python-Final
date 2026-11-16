#Imparitive approach

a = 22
b = 43

(a + b)

#Functional approach

def addition(a, b):
    print(a + b)

addition(21, 32)
addition(32, 43)

#object oriented programming approach

class Add:
    def __init__(self, a, b):
        print(a + b)

obj = Add(32, 54)

#Classes

class Factory:
    a = 12  # attribute

    def hello(self):  # method
        print("How are you")

    print("Hello how are you i am getting initialized")

print(Factory().a)
Factory().hello()

#Objects

class Factory:
    a = 12  # attribute

    def hello(self):  # method
        print("How are you")

    print("Hello how are you i am getting initialized")

obj = Factory()

print(obj.a)

#Constructor

class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"Your object details are {self.material}, {self.pockets}, {self.zips}")

reebok = Factory("leather", 4, 5)

campus = Factory("nylon", 6, 3)

reebok.show()

#Attributes and methods

#class attribute
class Animal:
    name = "lion" 

#Instance attribute 
    def __init__(self, age):
       self.age = age 

#Instance method
    def show(self):
       print(f"How are you your agger is {self.age}")

#class method
    @classmethod
    def hello(cls):
       print("How are you brother")

#Static method
    def static():
        print("How are you")

obj = Animal(12)

obj.show()

obj.static()
