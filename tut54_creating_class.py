class Student:
    pass
harry = Student()
Herminone = Student()

print(harry, Herminone) #shows that the objects are stored in different locations
#this shows that even though both use the same class, but are different objects

harry.name = "Harry"
harry.standard = "12th"
harry.section= "b"
Herminone.name = "Hermione"
Herminone.subjects = ["Hindi", "Physics"]
print(harry.name) #prints name of harry
print(harry.section, harry.standard)
# print(Herminone.standard) # this will give error as I have defined the standard yet
print(Herminone.subjects) #prints the list