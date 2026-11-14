from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:

       readfileandfolder()
       name = input("Enter the name of the file to create: ")
       path = Path(name)
       if not path.exists():

          with open(path, 'w') as f:
            data = input("Enter the data to write to the file: ")
            f.write(data)

          print(f"File '{name}' created successfully.")
       else:
          print(f"File '{name}' already exists.")

    except Exception as err:
        print(f"Sorry, there is an error: {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file to read: ")
        path = Path(name)
        if path.exists() and path.is_file():
          with open(path, 'r') as f:
            data = f.read()
            print(data)

            print(f"File '{name}' read successfully.")
        else:
             print(f"File '{name}' does not exist.")

    except Exception as err:
        print(f"Sorry, there is an error: {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file to update: ")
        path = Path(name)
        if path.exists() and path.is_file():
            print("Press 1 for changing the name of the file: ")
            print("Press 2 for overwriting data to the file: ")
            print("Press 3 for appending some content in your file: ")

            res = int(input("Enter your choice: "))

            if res == 1:
                name2 = input("Enter the new name of the file: ")
                path2 = Path(name2)
                path.rename(path2)

            if res == 2:
                with open(path, 'w') as f:
                    data = input("Enter the data to write to the file: ")
                    f.write(data)

            if res == 3:
                with open(path, 'a') as f:
                    data = input("Enter the data to append to the file: ")
                    f.write(" " + data)

    except Exception as err:
        print(f"Sorry, there is an error: {err}")

def deletefile():
    try:
        name = input("which file you want to delete: ")
        path = Path(name)

        if path.exists() and path.is_file():
            os.remove(path)

            print("File removes successfully")

        else:
            print("No such, file exist")

    except Exception as err:
        print(f"An error occured as {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Enter your choice: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()
