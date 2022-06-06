def function_prints_name(a,b,c,d):
    print(a,b,c,d)
# function_prints_name("Hermione", "Ron", "Ginny", "Fred")
#here if I add one more name to the function by adding one more argument, the function wont take it
#this is because we made the function to specifically take only 4 arguments
#this can be solved only if we edit the original function

#instead of doing that,

def function_args(normal, *args): #the function can also take normal arguments with the args as well
    print(normal)
    for item in args:
        print(item) #prints individual items in the list of har
#args is depicted by the keyword with the star
    print(type(args)) #the argument is taken as tuple in every case
    print(args[0]) #prints the first element of the list

#add the names in list and then pass the list containing the names in the function instead of adding one by one name
names = ["Hermione", "Ron", "Ginny", "Fred","Program"]
normal = "I am a normal argument"
function_args(normal, *names) #the star sends all the contents of har inside the function
#so just adding the name in the list simply will make that name print too instead of going all the way to the function as well

def function_args2(*name_can_be_anything):
    print(name_can_be_anything[0])

list2 = ["Hermione", "Ron", "Ginny", "Fred", "Program"]
function_args2(*list2)

#but
#THE CONVENTION:
#we have to pass the normal argument first and then the args
# def function_args2(*name_can_be_anything, normal):

#-----------------------------USE OF KWARGS-------------------------------------------

def function_args3(normal, *name_can_be_anything, **kwargs_program_wala):
    print(normal)
    for item in name_can_be_anything:
        print(item)
    print("Now I would introduce")
    #really like this one, def going to use it aage
    for key, value in kwargs_program_wala.items():
        print(f"{key} is a {value}")

kw = {"Rohan":"Monitor", "Harry":"Instructor", "Programmer":"Shweta", "cook": "Shivam"}
#i added cook and the change was reflected in the function used for printing the key along with its value
function_args3(normal, *list2, **kw)
