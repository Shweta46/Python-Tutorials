def printher(string):
    return f"This string is returned to us {string}"

def add(num1, num2):
    #a false addition function
    return num1 + num2 + 5

#the main function, used here, will help the file, which imports this file, in proper execution

print("and the name is", __name__)
#here, when we print the above statement this prints, as __main__
#when we import this and run the file, the name will be the name of the file from which it was imported
if __name__ == '__main__':
    print(printher("Hermione"))
    o = add(4, 6)
    print(o)
#so, now back to executing the program in the other file
#the function inside the main function doesnt execute in other files which import this file
#this function doesnt affect the working of the current file that we are working on
