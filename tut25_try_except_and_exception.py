print("Enter number 1")
num1 = input()
print("Enter number 2")
num2 = input()
# print("The sum of the two numbers is",
#           int(num1)+int(num2))
# #if we enter the input other than integer it will show error and the next line wont print
# print("This line is very important")  #i want this line to execute nonetheless
# #to improve this and have an exception to the type of the input we are taking which is integer in this case and printing the important line
# #we use try and except
try:
    print("The sum of the two numbers is",
          int(num1)+int(num2))
except  Exception as e: #here e is taken as the exception and the program still runs succesully
    #so whatever invalid input we enter it is assigned to e and e is printed
    print(e)
print("This line is very important")
# used when we want to run the program even when the inputs are not valid
# and to accept the exception and dont let the program quit in the middle
