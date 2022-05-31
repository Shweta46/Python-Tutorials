f = open("text.txt")
# print(f.readline()) #reads first line
# print(f.readline()) #reads the next line and displays it at the output
# # to know at which character the file pointer, which is f in this case, is- f.tell is used
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
#this prints the line and the pointer position

# now if we want to reset my file pointer to the very first line
print(f.readline())
f.seek(10) #here 10 is the position we want the pointer to start reading the file from or any operation we want
print(f.tell())
print(f.readline()) #prints 10 as the pointer is at 10
#the command from 12 to 15 prints the first line of the text file two times as the pointer is back to the top
f.close() #close the file at all times!!!!!!!

