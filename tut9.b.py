numbers = [2, 7, 9, 11, 3]
numbers[1] = 98
print(numbers)#replaces the number in first index with 98

#Mutable = Can change
#Immutable = Cannot change

tp = (1, 2, 3)
print(tp)#prints the tp with the paranthesis but the list was showing [] so its not a list but a tuple
#tp[1] = 8 #this gives error as tuple is immutable
#print(tp)

print('\n')
tp4 = ()
print(type(tp4))
tp2 = (1)
print(type(tp2))#this tells you that tp2 is of type class = int
print(tp2)#when a tuple has only one element then there are no parathesis printed along with it and so it isnt a tuple
print('\n')
tp3 = (1,)#tuple with one element needs one extra comma to be considered a tuple
print(type(tp3))
#SWAPPING THROUHG CONVENTIONAL METHOD
a=1
b=8
'''temp = a
a=b
b=temp
'''
#SWAPPING USING PYTHON METHOD
a,b = b, a
print(a, b)