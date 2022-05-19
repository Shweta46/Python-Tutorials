d1 = set()#making a class set which is a collection of well defined objects
d2=()
d3={}
d4=[]
print(type(d1))
print(type(d2))
print(type(d3))
print(type(d4))
s= set()#set is easily made using lists
l= [1,2,3,4]
print(type(s))
s_from_list = set(l)
print(s_from_list)#the elements print in curl brackets
print(type(s_from_list))

s.add(1)
print(s)#set only retains unique value so adding one more 1 wont affect the set
#if i add another value other than 1, then it is updated and added in the set
s.add(2)
s.add(1)#not added in the set as 1 is already there
print(s)
s.union({1,2,4})
print(s)
s1 = s.union({1,2,3,4})#union adds elements in the set but only 3 is added in the set
print(s, s1)
s2 = s.intersection({1,2,3})#prints a set whose elements are common with that of s
print(s, s2)
print(len(s))
print(max(s))
print(min(s))
s3 = {4,6}
print(s.isdisjoint(s3))#A pair of sets which does not have any common element are called disjoint sets
#in the above, we are checking is s is disjoint with s3 or not
