class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    # def print_details(self):
    #     return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    #
    # @classmethod
    # def changes_leaves(cls, new_leaves): #cls appeared instead of self, as classmethod is used for this purpose only
    #     cls.no_of_leaves = new_leaves

    @classmethod
    def from_str(cls, string): #instead of passing arugments in the class and writing it properly like we are doing in init,
# we can directly use string as an argument to define individual attributes of the object
        params = string.split("-") #splits the string when "-" comes makes it into a list which has different items
        print(params) #prints a list with 3 items in the string which are separated by "-"
        return cls(params[0], params[1], params[2]) #for this to work, the class should be enabled to take arguments, using the init function above

    #can also be represented as a one liner
    @classmethod
    def one_liner_from_string(cls, strings):
        return cls(*strings.split("-"))

harry = Employee("Harry", 455, "Instructor")
Hermione = Employee("Hermione", "15Lakhs", "Student")
# karan = Employee("Karan-480-Student") #will show error and we still have to give two more arguments to this function
#to solve this
karan = Employee.from_str("Karan-480-Student") #this is used when the data available is of the form which is split using "-" in between and to be made in a readable data
arjun = Employee.one_liner_from_string("Arjun-15lakhs-Employee")
print(harry.no_of_leaves)
print(karan.salary)
print(arjun.role)
