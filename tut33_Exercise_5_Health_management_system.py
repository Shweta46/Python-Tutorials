# #Health Management System#
#
# #3 Clients - Harry, Rohan and Hammad
# #design - diet and exercise
# #so total 6 files should be created to record the food that they are eating and the exercise they are doing
# #write a function that when executed takes input as the client name: say press 1 for harry, 2 for Rohan and 3 for hammad
# #lets say I chose 1: then ask what do you want to record for today? Diet or exercise? so 1 for diet and 2 for exercise
# #whatever I will write is printed
#
# #use the function
# # def getdate():
# #     import datetime
# #     return datetime.datetime.now()
# # print the time first inside square brackets like these [], then diet and then exercise
#
# #one more function to retrieve exercise or food for any client
# #so first retrieve or lock? Then whose? then what to lock? diet or exercise? then we write it
#
from scipy.constants import value
dore1 = {1 :'Roshan', 2:'Harry', 3:'Larry'}
dore2 = {1 :'Diet', 0:'Exercise'}
def getdate():
    import datetime
    return datetime.datetime.now()

def printthis():
  print("Hello from a function")

def lockorretreive():
    if action == 1:
        while True:
            ans = int(input("Name for retrieval? \n 1 = Harry \n 2 = Roshan \n 3 = Larry\n"))
            if ans == 1 or ans == 2 or ans == 3:
                name = True
                dore = input(print("Enter what to retrieve: Diet = 1 or Exercise = 0?\n"))
                # print(retreive1())
                break
            else:
                print("\nPlease enter a valid response...\n")

    elif action == 2:
        while True:
            ans = int(input("Name for log? \n 1 = Harry \n 2 = Roshan \n 3 = Larry\n"))
            # print("The log is chosen for " + dore1.get(ans))
            if ans == 1 or ans == 2 or ans == 3:
                name = True
                print("Enter what to log: Diet = 1 or Exercise = 0?\n")
                dore = int(input())
                # print("The log chosen is" + dore2.get(dore))
                if ans == 1 and dore == 1:
                    printthis()
                    with open("Roshan_diet.txt", "a+") as f1:
                        a = f1.write(input())
                        f1.seek(0)
                        b = f1.read()
                        getdate()
                        print(b)
                        return a
                elif ans == 2 and dore == 1:
                    printthis()
                    with open("Harry_diet.txt", "a+") as f1:
                        a = f1.write(input())
                        f1.seek(0)
                        b = f1.read()
                        print(getdate())
                        print(b)
                        print(a)
                elif ans == 3 and dore == 1:
                    printthis()
                    with open("Larry_diet.txt", "a+") as f1:
                        a = f1.write(input())
                        f1.seek(0)
                        b = f1.read()
                        print(getdate())
                        print(b)
                        print(a)
                elif ans == 1 and dore == 0:
                    printthis()
                    with open("Roshan_exercise.txt", "a+") as f1:
                        a = f1.write(input())
                        f1.seek(0)
                        b = f1.read()
                        print(getdate())
                        print(b)
                        print(a)
                elif ans == 2 and dore == 0:
                    printthis()
                    with open("Harry_exercise.txt", "a+") as f1:
                        a = f1.write(input())
                        f1.seek(0)
                        b = f1.read()
                        print(getdate())
                        print(b)
                        print(a)
                elif ans == 3 and dore == 0:
                    printthis()
                    with open("Larry_exercise.txt", "a+") as f1:
                        a = f1.write(input())
                        f1.seek(0)
                        b = f1.read()
                        print(getdate())
                        print(b)
                        print(a)
                else:
                    print("Please enter a valid response...")
                break
            else:
                print("\nPlease enter a valid response...\n")

print("Do you want to retrieve the information or lock?")
# action = int(input("Enter 1 for retrieve and 2 for lock\n"))
actions = ['1', '2']
action = None
while action not in actions:
    print("Enter 1 for retrieve and 2 for lock")
    action = int(input())
    lockorretreive()
    # if answer == 1 or answer == 2:
    #     lockorretreive()
    #     break
    # else:
    #     answer = input('Please enter a valid response...')
    #     continue



# def retreive1():
#     if ans == 1 and dore == 1:
#         with open("Roshan_diet.txt", "r") as f1:
#             print([getdate()])
#             a = f1.read()
#             return a
#     elif ans == 2 and dore == 1:
#         with open("Harry_diet.txt", "r") as f1:
#             print([getdate()])
#             a = f1.read()
#             return a
#     elif ans == 3 and dore == 1:
#         with open("Larry_diet.txt", "r") as f1:
#             print([getdate()])
#             a = f1.read()
#             return a
#     elif ans == 1 and dore == 0:
#         with open("Roshan_exercise.txt", "r") as f1:
#             print([getdate()])
#             a = f1.read()
#             return a
#     elif ans == 2 and dore == 0:
#         with open("Harry_exercise.txt", "r") as f1:
#             print([getdate()])
#             a = f1.read()
#             return a
#     elif ans == 3 and dore == 0:
#         with open("Larry_exercise.txt", "r") as f1:
#             print([getdate()])
#             a = f1.read()
#             return a
#     else:
#         print("Please enter a valid response...")


# def log1():
#     if ans == 1 and dore == 1:
#         with open("Roshan_diet.txt", "a") as f1:
#             a = f1.write(input())
#             b = f1.read()
#             print(b)
#             print([getdate()])
#             return a
#     elif ans == 2 and dore == 1:
#         with open("Harry_diet.txt", "a") as f1:
#             a = f1.write(input())
#             b = f1.read()
#             print(b)
#             print([getdate()])
#             return a
#     elif ans == 3 and dore == 1:
#         with open("Larry_diet.txt", "a") as f1:
#             a = f1.write(input())
#             b = f1.read()
#             print(b)
#             print([getdate()])
#             return a
#     elif ans == 1 and dore == 0:
#         with open("Roshan_exercise.txt", "a") as f1:
#             a = f1.write(input())
#             b = f1.read()
#             print(b)
#             print([getdate()])
#             return a
#     elif ans == 2 and dore == 0:
#         with open("Harry_exercise.txt", "a") as f1:
#             a = f1.write(input())
#             b = f1.read()
#             print(b)
#             print([getdate()])
#             return a
#     elif ans == 3 and dore == 0:
#         with open("Larry_exercise.txt", "r") as f1:
#             a = f1.write(input())
#             b = f1.read()
#             print(b)
#             print([getdate()])
#             return a
#     else:
#         print("Please enter a valid response...")



# def function1(a):
#     if clients == 1 and data == 1:
#         f1 = open("Roshan_diet.txt", "r")
#         a = f1.read()
#         print([getdate()])
#         return a
#     elif clients == 2 and data == 1:
#         f2 = open("Harry_diet.txt", "r")
#         a = f2.read()
#         print([getdate()])
#         return a
#     elif clients == 3 and data == 1:
#         f3 = open("Larry_diet.txt", "r")
#         a = f3.read()
#         print([getdate()])
#         return a
#     elif clients == 1 and data == 0:
#         f1 = open("Roshan_exercise.txt", "r")
#         a = f1.read()
#         print([getdate()])
#         return a
#     elif clients == 2 and data == 0:
#         f2 = open("Harry_exercise.txt", "r")
#         a = f2.read()
#         print([getdate()])
#         return a
#     elif clients == 3 and data == 0:
#         f3 = open("Larry_exercise.txt", "r")
#         a = f3.read()
#         print([getdate()])
#         return a
#
# def function2(action):
#     if clients == 1 and data == 1:
#         f1 = open("Roshan_diet.txt", "a")
#         a = f1.write(input())
#         print([getdate()])
#         return a
#
#     elif clients == 2 and data == 1:
#         f2 = open("Harry_diet.txt", "a")
#         a = f2.write(input())
#         print([getdate()])
#         return a
#     elif clients == 3 and data == 1:
#         f3 = open("Larry_diet.txt", "a")
#         a = f3.write(input())
#         print([getdate()])
#         return a
#     elif clients == 1 and data == 0:
#         f1 = open("Roshan_exercise.txt", "a")
#         a = f1.write(input())
#         print([getdate()])
#         return a
#     elif clients == 2 and data == 0:
#         f2 = open("Harry_exercise.txt", "a")
#         a = f2.write(input())
#         print([getdate()])
#         return a
#     elif clients == 3 and data == 0:
#         f3 = open("Larry_exercise.txt", "a")
#         a = f3.write(input())
#         print([getdate()])
#         return a


#can be correct but doesnt print the "Not a valid response" message, just repeats until the entered value is valid
    # answers = ['1', '2', '3']
    # answer = None
    # while answer not in answers:
    #     print("Name for retrieval? \n 1 = Harry \n 2 = Roshan \n 3 = Larry\n")
    #     answer = int(input())
    #     if answer == 1 or answer == 2 or answer == 3:
    #         break
    #     else:
    #         answer = input('Please enter a valid response...')
    #         continue
    # print("Enter what to lock: Diet = 1 or Exercise = 0?\n")

