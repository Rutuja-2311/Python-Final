a = open("hello.txt", "w")
a.write("This is a test file.")
a.close()

a = open("hello.txt", "a")
a.write("\nThis is an appended line.")
a.close()

a = open("hello.txt", "r")
print(a.read())
a.close()
