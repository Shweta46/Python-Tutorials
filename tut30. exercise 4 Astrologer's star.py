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
# i = 0
# n = int(input("Enter the number of rows in the pattern"))
# var = int(input("Enter the Boolean variable, 1 or 0"))
# while(True):
#     if i < n and var == 1:
#         print('*'*(i+1))
#         # print("\n")
#         i = i + 1
#         if i == n:
#             break
#     elif i < n and var == 0:
#         print('*'*(n-i))
#         # print("\n")
#         i = i + 1
#         if i == n:
#             break

#OR
# for i in range(n):
#     if var == 1:
#         print("*"*i)
#         while (i == n):
#             break
#     elif var == 0:
#         print("*"*(n-i))
#         while (i == n):
#             break

# OR;
# if var == 1:
#     for i in range(0, n):
#         print("*"*i)
# elif var == 0:
#     for i in range(n, 0, -1):
#         print("*"*i)

#OR
while(True):
    i = 0
    n = int(input("Enter the number of rows in the pattern"))
    var = int(input("Enter the Boolean variable, 1 or 0"))
    try:
        if var == 1:
            for i in range(0, n):
                print("*" * i)
            break
        elif var == 0:
            for i in range(n, 0, -1):
                print("*" * i)
            break
    except Exception as e:
        print("Please enter a valid response...")

#OR
# n = int(input("Enter the number of rows in the pattern"))
# var = int(input("Enter the Boolean variable, 1 or 0"))
# def star(n, var):
#     if var == 1:
#         for i in range(0, n):
#             print("*" * i)
#     elif var == 0:
#         for i in range(n, 0, -1):
#             print("*" * i)
# star(n, var)





