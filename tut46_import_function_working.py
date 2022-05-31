# import sklearn
# h = 1 #comes under current scope which is global scope for the program at the moment
# print(sklearn.__version__)
# #gives the version of the module
#
# #can also be represented as
# import sklearn as sk #use the abbreviation for representing this
# print(sk.__version__)
#
# import sys
# print(sys.path) #prints the path that the program brings modules from
#its prints all the hierarchy that is used to fetch the module

#RandomForestClassifier is a class type
from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

#taking variables of file named harry here
import harry
#imports a python file from the folder and it can display its content here
#here, a = 7 was added in harry.py file along with printing of Hello World
#so that whole program runs here along with printing the value of a which was simply a= 7 in harry.py file
#not print(a=7)
#so the file here, printed everything in the program here that was supposed to print
print(harry.a)

#to directly use the value a
from harry import a
print(a) #this simply prints 7

#the first method is a better than the second one, doesnt confuse you
#Now adding a function in the harry file called printjoke
# then

harry.printjoke("This is me")
#the function made in the harry file can be used using this and arguements can be passed by normal method that we generally use

#the already defined modules shouldnt be used as a file name as the modules search for the function inside that file first
#that file wont have any modules/function defined that we are looking for, so it will show error


