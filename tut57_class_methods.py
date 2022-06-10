class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def print_details(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def changes_leaves(cls, new_leaves): #cls appeared instead of self, as classmethod is used for this purpose only
        cls.no_of_leaves = new_leaves



# harry = Employee()
# rohan = Employee()
# harry.name = "Harry"
# rohan.name = "Rohan"
# harry.salary = "15L"
# rohan.salary = "17L"
# harry.role = "Student"
# rohan.role = "Student"
# print(rohan.print_details())
harry = Employee("Harry", 455, "Instructor")
Hermione = Employee("Hermione", "15Lakhs", "Student")
print(harry.salary)
print(harry.print_details())
print(Hermione.salary)
Employee.no_of_leaves = 89 #changes the no_of_leaves for the whole class and reflects in objects that use this variable
print(Hermione.no_of_leaves)

# harry.changes_leaves(34)  #changes the class variables when accessed through cls wala function
# print(harry.no_of_leaves) #shows now the no_of_leaves as 34 instead of 89 as it is changed due to the line above
#it can also be
Employee.changes_leaves(34)
print(harry.no_of_leaves)