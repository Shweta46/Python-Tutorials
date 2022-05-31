#Lambda functions or anonymous functions:
#it is a one line function
# def add(a,b):
#     return a+b
minus = lambda x, y: x-y
# def minus(x,y):
#     return x-y
print(minus(9,4))

def a_first(a):
    return a[1] #returns by sorting the list on the basis of the second element of the list
    return a #returning the first index of the element a going in the function
#so when we sort the list of list of a through the above function, the list is sorted on the basis of the first element of the list
#here, 0, 1 is how the indexing happens, so when finally sorting is done and then the function is called,
#the output is 6, 14 and then 23 and the respective pairs
a = [[1,14],[8,6], [4,23]]
# a.sort(key=a_first)
# print(a)
a.sort(key=lambda x:x[1]) #this is a one line function which returns the sorte function on the basis of its second element
print(a)