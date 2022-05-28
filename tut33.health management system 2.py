#Simple program
print("Do you want to retrieve the information or lock?\n "
                   "Enter 1 for retrieve and 2 for lock\n")
action = int(input())

def getdate():
    import datetime
    return datetime.datetime.now()

def function1(a):
    print("Name for retrieval? \n 1 = Harry \n 2 = Roshan \n 3 = Larry\n")
    clients = int(input())
    data = int(input("Enter what to retrieve: Diet = 1 or Exercise = 0?\n"))
    if clients == 1 and data == 1:
        f1 = open("Roshan_diet.txt", "r")
        a = f1.read()
        print([getdate()])
        return a
    elif clients == 2 and data == 1:
        f2 = open("Harry_diet.txt", "r")
        a = f2.read()
        print([getdate()])
        return a
    elif clients == 3 and data == 1:
        f3 = open("Larry_diet.txt", "r")
        a = f3.read()
        print([getdate()])
        return a
    elif clients == 1 and data == 0:
        f1 = open("Roshan_exercise.txt", "r")
        a = f1.read()
        print([getdate()])
        return a
    elif clients == 2 and data == 0:
        f2 = open("Harry_exercise.txt", "r")
        a = f2.read()
        print([getdate()])
        return a
    elif clients == 3 and data == 0:
        f3 = open("Larry_exercise.txt", "r")
        a = f3.read()
        print([getdate()])
        return a

def function2(action):
    print("Name for writing? \n 1 = Harry \n 2 = Roshan \n 3 = Larry\n")
    clients = int(input())
    data = int(input("Enter what to lock: Diet = 1 or Exercise = 0?\n"))
    if clients == 1 and data == 1:
        f1 = open("Roshan_diet.txt", "a")
        a = f1.write(input())
        print([getdate()])
        return a

    elif clients == 2 and data == 1:
        f2 = open("Harry_diet.txt", "a")
        a = f2.write(input())
        print([getdate()])
        return a
    elif clients == 3 and data == 1:
        f3 = open("Larry_diet.txt", "a")
        a = f3.write(input())
        print([getdate()])
        return a
    elif clients == 1 and data == 0:
        f1 = open("Roshan_exercise.txt", "a")
        a = f1.write(input())
        print([getdate()])
        return a
    elif clients == 2 and data == 0:
        f2 = open("Harry_exercise.txt", "a")
        a = f2.write(input())
        print([getdate()])
        return a
    elif clients == 3 and data == 0:
        f3 = open("Larry_exercise.txt", "a")
        a = f3.write(input())
        print([getdate()])
        return a

if action == 1:
    a1 = function1(action)
    print(a1)
    print(getdate())
elif action == 2:
    a1 = function2(action)
    print(a1)
    print(getdate())