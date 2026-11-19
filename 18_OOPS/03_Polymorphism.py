#Method override
class Animal:
    def show(self):
        print("Hello I am akarsh")

class Human(Animal):
    def show(self):
        print("How are you")

obj = Human()
obj.show()

#Method Overloading Not in Python

class Animal:
    def show(self):
        print("Hello I am akarsh")

    def show(self, name):
        pass

class Human(Animal):
    def show(self):
        print("How are you")

obj = Human()
obj.show()

#Duck Typing

class Animal:
    def show(self):
        print("I am showing")

class Human:
    def show(self):
        print("Hello I am also showing")

obj = Animal()
obj2 = Human()

obj.show()
obj2.show()
