#design a program that will make you guess a predefined number and tells you how close you are to this number
#number of guesses limited to 9
#print no. of guesses left
#when done with number of guesses print game over!
# i = 0
# n = 18
# while(True):
#     inp = int(input("Enter a number\n"))
#     if inp > n:
#         print("the number is smaller than this")
#         i = i + 1
#         print("Number of guesses left =", 5 - i)
#         if i == 5:
#             print("Game over!")
#             break
#     elif inp < n:
#         print("the number is greater than this")
#         i = i + 1
#         print("Number of guesses left =", 5 - i)
#         if i == 5:
#             print("Game over!")
#             break
#     elif inp == n:
#         print("Congrats! This is the number")
#         i = i+1
#         print("Number of guesses you took to win", i)
#         i = 0
#         break
#
# # or
a = 18
for i in range(1,10):
    n=int(input("Guess the number"))
    if i< 9 or n==18:
        if n< a:
            print("Number is higher")
            print("Remaining guess", 9-i)
        elif n> a:
            print("Number is lower")
            print("Remaining guesses", 9-i)
        else:
            print("Congratulations! You guessed the right number")
            print("No of guesses you took", i)
            break
    else:
        print("Remaining guesses", 9-i)
        print("Game Over!")
