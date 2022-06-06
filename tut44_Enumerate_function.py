l1 = ["Bhindi", "Aloo", "Momos", "Sphagetti"]
#to only select the odd items in the list
i = 1
for item in l1:
    if i%2 is not 0:
    # can also be i%2 !=0
        print(f"Jarvis please buy {item}")
    i += 1
#will print Jarvis please by item 1 and then Jarvis please buy item 3

#to print the same thing as above using enumerate function
# here index is value of index representing the items in the list
# The function helps in including the index and the item in the list as a one line statement and we dont have to mention i as a different var and then increase its value with i +=1
#the function does it automatically
for index, item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis please buy {item}")
#the length of the program is shorter in enumerate than the normal if condition we were using before


