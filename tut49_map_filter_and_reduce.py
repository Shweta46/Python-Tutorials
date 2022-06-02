#---------------map function: -----------------

# it applies a function to a whole list
numbers = ["3", "4", "5", "6"]
#all items in the list are strings, not integer

# numbers[3] = numbers[2] + 1
#above line will show error can only concatenate str (not "int") to str
#its because the number 1 is integer and numbers in "numbers" list are strings
#so,

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#     #this will convert all the strings in the list numbers to integers
# numbers[1] = numbers[1] + 1
# print(numbers[1])
#this adds 1 to the 2nd element of list

#the above thing can happen by using map function
#syntax is map("the function which needs to be applied to all elements of the list")
print(map(int, numbers)) #shows that map is an object at the memory location
numbers = list(map(int, numbers))
numbers[1] = numbers[1] + 1 #now since the numbers in list are all converted to integers, then 1 can be added to it
print(numbers[1])

def sq(a):
    return a*a

num = [2,3,45,7,8,23,78,9]
square = list(map(sq, num))
print(square) #shows the list of squared numbers of num list

# also, lambda function, which is a one liner function, can also be used here
square_other_way = list(map(lambda x: x*x, num))
print(square_other_way)

#applying more than one functions to all the elements of the list

def cube(a):
    return a*a*a
func = [sq, cube]
# num = [2,3,45,7,8,23,78,9]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)
#this will return the func[i] that is [sq[i], cube[i]]
#hence, [0, 0], [1,1], [4, 8], etc. will be returned

#-------------------------FILTER FUNCTION------------------------

#it filter things, makes a list of elements which returns true for a specific function

list1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num1):
    return num1>5

#returns true is number is greater than 5 and returns false when its not
print(is_greater_5(7)) #returns True

gr_than_5 = list(filter(is_greater_5, list1)) #typecasted into list to return some value
print(gr_than_5) #returns a list made up of elements in list1 that are greater than 5
#so, it filtered out the elements which stood true for the function

#-----------------------return-------------------------

from functools import reduce
list2 = [1,2,3,4]
num3 = 0
for i in list2:
    num3 = num3 + i
print(num3)
#this adds the elements in list2 together and prints the whole sum
#or this can happen in other way as well
num3 = reduce(lambda x,y: x+y, list2)
print(num3)
