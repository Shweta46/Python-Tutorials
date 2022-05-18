mystr = "Stars are infinity but moon is only one, you are my moon"
print(mystr)
print(mystr[4])#prints s or fourth character of the string
print(mystr[1:5])# to include all the letters from 0 to 5,we type this so whole "Stars" word will be included
#this above thing is called string slicing, in the above example only "tars" will be printed
print(len(mystr))#prints the length of the whole string which is 0 to 55 in this case

#print(mystr[78])#gives error as 78 is not any character in the string

print(mystr[0:78])#does not give error but gives the whole string

print(mystr[0:5:3])#prints the first 5 but skips every 2 characters in between
print(mystr[0:])#prints the whole string
print(mystr[:5])#takes it as [0:5] and hence prints the first 5 characters of the string
print(mystr[:])#prints the whole thing
print(mystr[::])#prints the whole thing as it takes it as [0:1:1]

print(mystr[:19:1])#takes the string from starting and doesnt skips any characteres
print(mystr[:57:5])#prints the whole string but skips 4  character in between
print('\n')
#Negative indices
print(mystr[-1:])#printed the last character of the string
print(mystr[-4:-2])#prints the value from behind and they are negative indices and prints from -4 to -2

print(mystr[::-1])#reverses the string
print(mystr[::-2])#reverses the string but skips the character by 1

