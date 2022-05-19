#quiz = design a faulty calculator with
#computations 45*3 = 555, 56+9 = 77 and 56/6=4 to be incorrect calculations
#inputs from the users should be operator and the two numbers in which calculation needs to be done
#Design a calculator which will correctly solve all the problems except the ones above
print("Enter first number")
num1 = int(input())
print("Enter second number")
num2 = int(input())
print("Enter the operator")
op = input("Choose a math operation (+, -, *): ")
if (num1 == 45 and num2 == 3) or (num1 ==3 and num2 ==45):
    if op == '*':
        output = 555
        print(output)
elif (num1 == 56 and num2 == 9) or (num1 ==9 and num2 ==56):
    if op == '+':
        output = 77
        print(output)
elif (num1 == 56 and num2 == 6) or (num1 ==6 and num2 ==56):
    if op == '/':
        output = 4
        print(output)
else:
    if op== '+':
        print(num1 + num2)
    elif op == '-':
        print(num1-num2)
    elif op== '/':
        print(num1/num2)
    elif op=='*':
        print(num1*num2)


