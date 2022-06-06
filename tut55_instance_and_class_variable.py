class Employee: #the first letter of the class should be capital, nice practice
    no_of_leaves = 8 #all the objects belonging to this class will have this as the set number of leaves
    #that will be the common leaves for everybody
    #this property can be accessed with the help of objects that use this
    #for example, like line 19
    pass

harry = Employee()
rohan = Employee()
harry.name = "Harry"
rohan.name = "Rohan"
harry.salary = "15L"
rohan.salary = "17L"
harry.role = "Student"
rohan.role = "Student"
print(rohan.name, harry.salary)
print(Employee.no_of_leaves)
print(harry.no_of_leaves)
#now lets try and change the no of leaves in Employee class using rohan object
print(rohan.__dict__) #prints all the attributes of the object rohan, but here there will no no_of_leaves attribute
rohan.no_of_leaves = 9
print(rohan.__dict__) #this will create an object instance and now no_of_leaves will be part of that attribute unlike before
print(Employee.no_of_leaves) #this prints 8 anyways
#because line 21 means, we created a new instance variable and its the property of an object itself not the whole class
#main class itself can its property, not the object using it
print(Employee.__dict__) #prints all the attributes of employee
#all the variables in Employee class will be shared by its objects