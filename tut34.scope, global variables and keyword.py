l = 10 #this is global variable that is can be used by any function in the program
def function1(n):
    # l = 5 #this is a local variable and can be used only by the function itself
    #first it looks if the variable is locally stored or not, then it looks for global variable
    m = 8
    #l, when a global variable, is a read only variable
    # l = l + 45 #we are trying to change here the value of global variable which is not possible
    global l #to take the permission to change a global variable
    #after using the above statement, the line 7 statement will not show error like before
    l = l + 45 #prints 55 and changes the value of l globally to 55, now the updated value of l globally is 55
    print(l, m) #if I comment out the l = 5 in line 3 then this will print l=10
    print(n, "I have printed")

print(l) #l printed is 10 not 5 as globally its value was 10
function1("This is me")
# print(m) #m is defined inside the function so this will show error

def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)
harry()
#the above program prints 20 and 20 before and after calling rohan even after taking global permission, Why?
#this happens because when we use global, it goes out of the program to see the value of x
#then updates it, here x is not present globally but inside the harry function in which its value is 20, so it prints that both the times
#now

#Quiz
x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)
harry()
print(x) #what will be the value of this x?. Initial guess: 88
#and the guess was correct