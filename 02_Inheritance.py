#Syntax 
class Factorymumbai:  #parent class/ super class
    a = "I am an attribute mentioned inside Factory"
    def hello(self):
        print("hello I am a method mentioned inside Factory")

class Factorypune(Factorymumbai):   #child class/ subclass
    pass

obj = Factorymumbai()

obj2 = Factorypune()

#print(obj.a)

print(obj2.hello())

#Constructor
class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Hello your name is {self.name}")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"hello your name is {self.name}, {self.age}")

animal1 = Animal("lion")
person1 = Human("Rutuja", 19)

person1.show()

#Types
#Multipal Inheritance

class Animal:
    name1 = "lion"

class Human:
    name2 = "Rutuja"

class Robots(Animal, Human):
    name3 = "charlie123"

obj = Robots()

print(obj.name3)

#Method Resolution order
class Animal:
    def __init__(self, name):
        pass

class Human:
    def __init__(self, name, age):
        pass

class Robots(Human, Animal):
    name3 = "charlie123"

obj = Robots("Rutuja", 19)

#Multilevel Inheritance

class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

obj = PuneFactory("cotton", 2, "blue", 4)

print(obj)