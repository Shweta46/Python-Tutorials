def function1():
    print("Subscribe Now")

func2 = function1
del function1 #if function1 is deleted after assigning it to func2, will the next statement still print?
func2() #answer is Yes.

def func_return(num):
    if num == 0:
        return print
    elif num ==1:
        return int #we can return functions inside a function as well
a = func_return(0)
print(a)

def executor(func):
    func("This")
executor(print) #this means that functions can be returned inside functions as an argument as well

def dec1(func1):
    def now_execute():
        print("Executing now")
        func1()
        print("func1 executed")
    return now_execute

#the line 31 wont even be necessary if we write this @dec1 before the function
@dec1
def who_is_hermione():
    print("She's a good girl.")
# who_is_hermione = dec1(who_is_hermione)

who_is_hermione()