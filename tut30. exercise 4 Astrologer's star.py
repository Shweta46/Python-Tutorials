#Pattern printing
#Input = Integer "n" where it represents no of rows in the pattern
# Boolean variable = can be 1 or 0 that is True or False
# so if Boolean variable = True
# for n = 5
# *
# **
# ***
# ****

# if boolean variable = False
# for n = 6
# ******
# *****
# ****
# ***
# **
# *
i = 0
n = int(input("Enter the number of rows in the pattern"))
var = int(input("Enter the Boolean variable, 1 or 0"))
while(True):
    if i < n and var == 1:
        print('*'*(i+1))
        # print("\n")
        i = i + 1
        if i == n:
            break
    elif i < n and var == 0:
        print('*'*(n-i))
        # print("\n")
        i = i + 1
        if i == n:
            break

# or
# def function1(a,b):
#     a = int(input("Enter the number of rows"))
#     b = int(input("Enter 0 or 1"))
#     for a in function1:
#         if b ==1:
#             print('*'*a)
#             a = a-1
#         elif b == 0:
#             print('*'* ())




