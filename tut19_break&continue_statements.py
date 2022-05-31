i=0
# while(True):
#     print(i, end ="")
#     i=i+1
#this will continue till many times
while(True):
    if i+1<5:
        i = i + 1
        continue #it will ignore all the statements below it if the conidtion is true and returns back to the while statement

    print(i+1, end=" ")
    if(i==44):
        break #used to stop the loop
    i = i + 1
#so the above program prints the numbers greater than 5 and less than or equal to 45
