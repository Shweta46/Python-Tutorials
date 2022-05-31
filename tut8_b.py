#STRING FUNCTIONS
mystr = "Harry is a good boy"
mystr2 = "Harryisagoodboy"
print(mystr.isalnum())#returns True if a string contains alphanumeric characters without any symbols
print(mystr.isalpha())#returns True is all characters in the string are letters but here it has space in between which is not a letter
print(mystr2.isnumeric())#returns True is a string contains only numbers
print(mystr2.isalpha())
print('\n')
print(mystr.endswith('boy'))
print(mystr.count('o'))#counts the number of o's in the string
print(mystr.find('is'))#finds the index from which is is starting with
print(mystr.lower())#the whole string is converted to lowercase
print(mystr.upper())# the whole string converted to uppercase
print(mystr.replace('is', 'are'))#the 'is' in the string is converted to 'are'
