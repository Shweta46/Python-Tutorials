#var is used to store things or variables or numbers
var1 = "Hello world"
var2 = 4
var3 = 36.7
var4 = "This is new"
var5 = "54"
var6 = "43"
#python automatically gives type to the variable
print(var1)
#this next one will define the variable type and print its type
print(type(var3))
print(var2)
print(var3)
print(var2+var3) #adds the numeric type variables
print(var1 + var4) #same type of variables are added
print(type(var3))

print(var5 + var6) #two strings are concatenated
print(int(var5)+int(var6))#int function type casts string to integer function
#other types are str(), int(), float()

#to print same word multiple times
print(10* "Hello world\n")
print(100*int(var5)+int(var6))#BODMAS is applied
print(1000*int(var5)+int(var3))
#to print the sum of numbers 100 times
print(1000* str(int(var5)+int(var6)))

#asks the user an option to give an input
print("Enter your number")
inpnum = input()
#print("you entered", inpnum)
#if
#print("You entered", inpnum+10)
#this wont give you 10 added to your input number as inpnum is a string

#you have to typecast inpnum from string to an integer first
print("You entered", int(inpnum)+10)#this gives 10 added to your added number
print("You entered", inpnum)