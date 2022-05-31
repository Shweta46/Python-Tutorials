list1 =["Harry", "Larry", "Carry", "Marie"] #list
print(list1[0:]) #to print all the items in the list above
for item in list1:
    print(item)
# if i have to print all the keys of a dictionary then
dict1 = {"harry":"marry", "carry": "larry", "copy":"sloppy"}
for keys in dict1:
    print(keys)

list2 = ("Harry", "Larry", "Carry", "Marie") #tuple
for item in list2:
    print(item)
#list of names and the amounts of cars they have
list3 = [["Harry", 1], ["Larry",2], ["Carry",3], ["Marie",4]] #list
for item in list3:
    print(item)
#the above item will be printed as a list of list
#now to print it as first name and then the number of cars owned then;
for item, car in list3:
    print(item, car)
#or
    print(item, 'and the cars they own is', car) #i like this way better

#to typecast the list to a dictionary, we can directly used dict keyword and write
dict2 = dict(list3)
print(dict2)
# for item, car in dict2:
#     print(item, car)
#the above command will give error or will give exit code 1 which means it is an invalild file
#so it should be instead
for item, car in dict2.items():
    print(item,'and the cars they own is', car)
    #the above command gives the output as obtained in line 20 or 22
    