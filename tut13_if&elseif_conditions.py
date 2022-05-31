var = 6
print(type(var))
var2= 56

var3= int(input()) #if we dont type cast this as int then it will be taken as string
#a string cant be compared to an integer so it will show error
print(type(var3))
#if is a keyword thats why represented with blue colour
#colon is used to enter inside a statement
if var3>var2:
    print("Greater")
if var3==var2:
    print("Equal")
else:
    print("Smaller")
#to not make the program check every statement after the statement stands true for an input
#we used elif instead of if repeatedly, this way if a statement is true then the program
# directly jumps to the statement after if-else conditions

var5=44
var6=int(input())
if var5<var6:
    print("Smaller")
elif var5==var6:
    print("Equal")
else:
    print("Greater")

list1 = [5,7,3] #to check if a number is present in the list "in" keyword is used
print(5 in list1) # this simply returns True if 5 is in the list
print(15 in list1)
print(6 not in list1)
if 5 in list1:
    print("Yes 5 is in the list")
