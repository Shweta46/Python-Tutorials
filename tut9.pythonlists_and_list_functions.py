#list is a list of things may be students and grocery list
grocery = ['Harpic', 'Vim bar', 'Deodrant', 'Bhindi', 'Lollypop', 56]
print(grocery)#prints the list with [] included at the start and at the end
print(grocery[0])#we get harpic as the output
print(grocery[5])#prints 56

numbers = [2, 7, 9, 11, 3]
print(numbers)#prints the numbers

print(numbers[2])
numbers.sort()#sorts the list
#numbers.reverse()#reverses the sorted list
print(numbers)#prints the sorted list
#numbers.reverse()
print(numbers[0:6])#slicing the list
print(numbers[:])#gives the whole list from 0 to 5th element
print(numbers[1:4])
#Functions change the original list but slicing doesnt do anything just gives output
print(numbers[::2])#skips the list by one item
print(numbers[::-2])#reverses the list and prints it by skipping 1 number
print(numbers[::-1])#reverses the list
print(numbers[1:5:-3])#gives off a blank list as the numbers are famished
print(numbers)
print(len(numbers))#gives the length of the list
print(min(numbers))#gives the minimum number in the list

#numbers.append(7)#adds the number 7 at the ed of the list
#numbers.append(45)
numbers.insert(1,67)#inserts the number 67 after the first index
print(numbers)
numbers.insert(3,45)#inserts the number after 3rd index
print(numbers)
numbers.remove(9)#removes the number 9 from the list
print(numbers)
numbers.pop()#removes the last number from the list that is pops it
print(numbers)
