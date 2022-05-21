# f = open("text2.txt", "w") #write mode
# f.write("The universe is generous to the ones who ask")
# f.close()
#this makes a file called text2.txt which has the text above
#if the file already existed, then the content will be replaced with the content above
#but in most of the cases, we want to append something to a file and not replace its content

# so for appending
# f = open("text2.txt","a")
# # f.write("This is added to the file \n")
# # f.close()
# #the line is appended to the text file as many times as we run this command
#
# #if we want to know how many characters we wrote, then
# a = f.write("Harry Potter is the boy chosen\n") #f.write function returns the no. of characters
# print(a)
# f.close()

#how to read and write both at the same time
f = open("text2.txt","r+") #r+ is doing reading and writing at the same time
print(f.read()) #reading the file
f.write("Thank you") #writes this text to the file and if you open the text file you will see this added
a = f.write("As you say")
print(a) #prints the characters added
f.close()

