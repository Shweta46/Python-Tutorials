age1 = 18
print("Enter your age")
age2 = int(input())
if age2<7:
    print("Please enter a valid age")
elif (age2>7 and age2<100):
    if age1<age2:
        print("You can legally drive")
    elif age1==age2:
        print("Can't decide, please come to the DMV to verify")
    else:
        print("You cannot legally drive")
elif age2>100:
    print("Please enter a valid age")