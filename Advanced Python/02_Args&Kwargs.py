#args

def add(*args):
    sum = 0
    for i in args:
        sum = sum + i

    print(sum)
    #print(args)

add(23,43,12,554,543,56)


#kwargs

def information(**kwargs):
    print("Your information is \n\n")
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")

information(name = "Rutuja", age = 19, designation = "Ai agentic" )
