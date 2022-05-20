#Take input from the user and print it until the number is > 100
#when it is greater than 100, print that you have a number greater than 100

# while(True):
#     print("Enter a number")
#     if int(input())>100:
#         print("You have finally entered a number greater than 100")
#         break
#or
while(True):
    inp = int(input("Enter a number\n"))
    if inp>100:
        print("Congrats you entered a number > 100\n")
        break
    else:
        print("Try again!\n")
