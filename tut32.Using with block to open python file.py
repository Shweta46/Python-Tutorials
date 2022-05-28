with open("text.txt") as f: #replaces the open and close statements we used to write before
#it opens and closes the file on its own
    a = f.read(4) #reads the first 4 characters of the text file
    print(a)

# question of the day: if we again open and close the file outside the with block and use the command readlines() will it print?
#initial guess - It should as we are opening the file again after closing it so the pointer should be at the begining
#actual result
f = open("text.txt")
print(f.readlines())
f.close()
