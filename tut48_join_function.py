list1 = ["John", "Jerry", "Jade", "Jason", "Jack", "Jackson", "Josh"]

for index, item in enumerate(list1):
    print(f"{item} and", end=" ")
print("\n")
# or
for item in list1:
    print(item, ",", end=" ")
print("other people with names starting with J")

#the output obtained from above statements can also be achieved using
a = ", ".join(list1) #this means join the items of the list list1 by inserting ", or and" between them
print(a, "and other people")
