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

    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        print(params)
        return cls(params[0], params[1], params[2])

    @classmethod
    def one_liner_from_string(cls, strings):
        return cls(*strings.split("-"))

    @staticmethod #a function that doesnt take class or self as an argument, but simply does its job
    def print_good(string):
        print("This is good." + string)
        return "This is good " + string

harry = Employee("Harry", 455, "Instructor")
Hermione = Employee("Hermione", "15Lakhs", "Student")
karan = Employee.from_str("Karan-480-Student")
arjun = Employee.one_liner_from_string("Arjun-15lakhs-Employee")

print(karan.no_of_leaves)

print(Hermione.print_good("Hermione"))
