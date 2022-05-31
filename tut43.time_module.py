import time
# lets you know the execution time of the program
initial = time.time() #returns a value of the initial time of the program
# print(initial)
k = 0
while(k<450):
    print("This is Hermione")
    time.sleep(2) #sort of like wait function in verilog
    #prints the text after 2 seconds each
    k +=1
print("While loop ran in", time.time() - initial, "second")

initial2 = time.time()
for i in range(450):
    print("This is Hermione!")
print("For loop ran in", time.time() - initial2, "second")

# import time

# get the start time
# st = time.time()
#
# # main program
# # find sum to first 1 million numbers
# sum_x = 0
# for i in range(1000000):
#     sum_x += i
#
# # wait for 3 seconds
# time.sleep(3)
# print('Sum of first 1 million numbers is:', sum_x)
#
# # get the end time
# et = time.time()

# get the execution time
# elapsed_time = et - st
# print('Execution time:', elapsed_time, 'seconds')

#giving time of the current location we are in
localtime = time.asctime(time.localtime((time.time())))
print(localtime)