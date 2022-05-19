#ASSIGNMENT
#create a dictionary, take input from the user and return the meaning of the word
d2 = {'Rage':'Really angry', 'Weep':'Cry badly', 'Skilled':'Gained knowledge of the art','Man':'Male human being', 'Bad':'Not good', 'Rude':'Being harsh'}
# one way to print the keys - print(d2.keys())
#second and a better way to print the keys:
for keys in d2:
    print(keys)
print("Enter the word you want to know the meaning of")
word = input()
print("Meaning of the word is:",d2.get(word))