# f = open("text.txt")
# content = f.read()
# print(content) #this prints the content of the file text
# #so first we open the file and then read it and assign it contents to a variable
# f.close() #a good practice, if a file is opened it should be closed
#this is done to free up the resources used up in opening the file and the program behaves as expected

f = open("text.txt", "rb") #reading the file in binary form
# content = f.read()
# print(content)
# f.close()

f2 = open("text.txt", "rt") #default mode, reading in text
# content2 = f2.read()
# print(content2)
# f2.close()
#
# f3 = open("text.txt")
# content3 = f3.read(3) # reads only first three characters of the text
# print(content3)
#
# content3 = f3.read(3) # reads the next three characters of the text after the first one
# print(content3)
# # f3.close()
#
# #to read line by line
# content4 = f3.read()
# for line in content4: #this prints the characters line by line, not what we wanted exactly
#     print(line)

# content5 = f.read()
# for line in f2:
#     print(line, end ="") #this wont print anything as content above in line 14 is already reading this file
#so we comment out the line 14

# print(f2.readline()) #prints the first line
# print(f2.readline()) #prints the next line
print(f2.readlines()) #prints a list with list of lines
