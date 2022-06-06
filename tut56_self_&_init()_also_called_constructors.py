class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self): #self = woh object jiski baat kee jaa rahi hai
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#the object that will be using the Employee classes's function will be replaced by self in this

# harry = Employee()
# rohan = Employee()
# harry.name = "Harry"
# rohan.name = "Rohan"
# harry.salary = "15L"
# rohan.salary = "17L"
# harry.role = "Student"
# rohan.role = "Student"
# print(rohan.print_details()) #so in the function print_details, rohan will be accepted as an argument
# # then it will print the name and salary and role that we have predefined for rohan
#
# print(harry.print_details()) #template is same, but the filled forms have different values
#you can just edit the function used by the objects and the final product used by the objects will contain the editted version
#without having to change the objects individually

#--------------------constructor----------------------------------

harry = Employee("Harry", 455, "Instructor") #without constructors, this shows the error Employee() takes no arguments
#to make the Employee class take arguments, we use constructors
#for that we use init
#to avail the function, we dont necessary have to call it, we just pass the arguments in the class itself and it will do the job
#for the line 31 to run successfully and not use any other program statements, we directly write this and comment out the lines above describing the individual values
print(harry.salary)