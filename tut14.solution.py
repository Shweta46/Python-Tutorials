items = [int, float, "Harry", 5, 2,3,21,25,9,3,1,90]
for item in items:
    #here typecasting is used as it will typecast  numerical numbers to string
    #and then check if the obtained string is or contains numeric number or value
    if str(item).isnumeric() and item>6:
        print(item)