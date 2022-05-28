# a = 9
# b = 8
# c = sum((a,b)) #build-in function
# print(c)

# def func1(a, b):
#     print("Hello you are in function", a+b)
# func1(5, 7)

#to store the output in variable
def func2(a, b):
    #the below mentioned in known as docstrings, it gives the definition what the function does
    """This is a function which calculates the average of two numbers
    This doesnt run for 3 number"""
    average = (a+b)/2
    # print(average)
    return average
v= func2(5, 7) #the value of return from the function is stored in v
print(v) #this prints the value of v which from the above line now stores the return value of output
print(func2.__doc__) #to print the docstring of the function mentioned
#usually, we print the docstrings of the function before we use it to define its usage
