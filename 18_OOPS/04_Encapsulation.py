class Factory:
    __a = "Pune"

    def show(self):
        print(Factory.__a)

#     def __show(self):
#         print("Hello i am a pune factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super().__a)

# obj = Bhopal()
obj = Factory()

obj.show()
