#make a list and any items an integer or string can be inside it
# detect if its a number or not, if yes then check if its is greater than 6 or not and if it then print the number

list1 = [3,7,8,10,1,5,16,'Syria','Japan','Russia','Belarus']
# for item in list1:
#     if type(item) == int:
#         if item > 6:
#             print(item)
#to make the program smaller
for item in list1:
    if type(item) == int and item > 6:
        print(item)