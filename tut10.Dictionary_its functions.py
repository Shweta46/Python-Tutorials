#Dictionary is a key-value pair that is a word (key) and its meaning (pair)
d1 = {}
print(type(d1))#the class comes as dict

d2 = {'Harry':'Burger', 'Rohan':'Fish', 'SkillF':'Roti',
      'Shubham':{'B':'Maggie','L':'Roti','D':'Chicken'}}
print(d2['Harry'])#prints the value of Harry that is Burger
print(d2['Shubham'])#prints the whole dict of Shubham
print(d2['Shubham']['B'])#prints maggie
d2['Ankit']= "Junk food"#adds ankit to d2 dict
print(d2)
d2['Sumit']='Sapoliya'
d2[420]= 'Kebab'
del d2[420]#removes the key 420 from d2 dict
#print(d2)

#d3 = d2#copying d2 to d3 so if we delete something from d3 it also gets deleted from d2
#del d3['Harry']
#print(d2)

d3 = d2.copy()#to prevent the deletion of elements from d2 when we deleted something from d3
#and to also copy d2 elements to d3 we create a copy of d2 and then assign that copy to d3
del d3["Rohan"]
print(d3)
print(d2)
print(d2.get('Harry'))

d2.update({'Leena':'Peena'})#updating the dict
print(d2)
print('\n')
print(d2.keys())#prints all the keys of the dict
print(d2.items())#prints all the key value pairs of dict
