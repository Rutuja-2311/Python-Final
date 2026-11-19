from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        print("I have created")
    
    def area(self):
        print("I have cretaed this")

class Square(abstract):
    def __init__(self, side):
        self.side = side

class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("I have created")

    def area(self):
        print("I have cretaed this")

obj = Circle(7)
obj2 = Square(12)
