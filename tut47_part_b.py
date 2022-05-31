# import tut47.if_name_equals_main_usage_and_necessity
#shouldnt also use full stops in your program, the import function thinks that "." means the name is complete
#also dont use "-"/ dashes in the program
#so i am going to rename my file now

import tut47_if_name_equals_main_usage_and_necessity
print(tut47_if_name_equals_main_usage_and_necessity.add(5,3))
#now if the file contained any other modules like we had included in it, the printing of the string and
#the sum 4 and 6 that we performed in it to see our function's working
#all the program in file will be executed in this file too, we dont want that
#when you import a file, it also executes all the functions in the file
#so, we use main function in the file that we imported

#when we use main function in other file, the content inside the main function doesnt execute when the file itself is imported by other files
#this function prints only the needed part, not all the program of the other file we imported
