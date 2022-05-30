#F-strings
me = "Hermione"
me2= "Conan"
me3= "Fallon"
me4 = "Gervais"
me5 = "Blake"
a = "This is %s" %me #this is string formatting
print(a)
#string formatting is useful when I want to insert a variable in a string
#if I have a very long string and want to insert many variables inside that string, then it would be difficult
a1 = "This is %s also %s and %s also %s"%(me, me2, me3, me4)
#while writing the above string we have to keep track of the %s and the me1 2 3 we used for it
#this is also not readable

#Now, we use string formatting
a2 = "This is {} {}"
b = a2.format(me, me2)
print(a1)
print(b)
#we can also define positions in the string, which word we want first and second and so on
a3 = "This is {1} {0}"
c = a3.format(me, me3) #this will print me3 first and then me
print(c)
#the readability is limited in the above formatting as well

#so f-strings were introduced
#write f before the string starts which abbreviates to fast
d = f"this is f string {me} {me2}" #this will directly print the value of variables inside {} bracket
print(d)

#also we can directly solve mathematical expression
e = f"this is f string {me} {me2} {4*50-5}"
print(e)

#we can also use functions inside string, first import the module and use the function
#example: math module
import math
f = f"this is f string {me} {me2} {math.cos(60)}"
print(f)

#use this when you want to mesh more than two strings together and increase the readability of the code
#object oriented programming
