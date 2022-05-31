#recursion is use of function inside a function
# def print2(str1):
#     print2(str1) #if we use this then it will show recursion error as we are using the function inside the function again and again
#
#     print("This is " + str1)
#
# print2("harry")

# n! = n * n-1 * n-2 * n-3....... * 1
# n1 = n * (n-1)!
def factorial(n): #this was not recursive function, this was iterative
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3....... * 1
        """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
number = int(input("Enter the number"))
print("using iterative method", factorial(number))

# using recurive function
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
# print("using recursive method", factorial_recursive(number))

#Quiz: Write fibanacci series
# 0 1 1 2 3 5 8 13

# def fibonacci2(n):
#     n1 = 0
#     n2 = 1
#     for i in range(n):
#         print(n1 + n2, end=" ")
#         return n1

def fibonacci(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print("using iterative method", factorial(number))
print("Fibonacci using iterative method", fibonacci(number))
# print("Fibonacci using recursive method", fibonacci2(number))

#what type of method should be used? Recurcive or iterative?
#iterative should be used