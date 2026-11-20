class Animal:
    @property
    def show(self):
        print("hello how are you")

obj = Animal()

obj.show

#Base of decorator

def decorate(func):
    def wrapper():
        print("I will print myself before the function hello")
        func()
        print("I will print after the function")
    return wrapper

@decorate
def hello():
    print("Hello I am Rutuja")

hello()

#

def decorate(func):
    def wrapper(a,b):
        print("the addition to your numbers are ")
        func(a,b)
        print("Thank you I hope you liked it")
    return wrapper

@decorate
def add(a, b):
    print(f"Your total is {a + b}")

add(32, 43)