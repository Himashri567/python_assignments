coun={"India","USA","England"}
coun.add("Peru") # adds Peru 
print(coun)
x= coun.copy()  #returns copy of the set
print(x)
x.clear() # removes all elements from the set x but the set exists
print(x)  
strings={"Hello","hii","hurray","India","USA"} 
z=coun.difference(strings) # returns items that are present in coun but not in strings
print(z)
strings.difference_update(coun)  # removes all elements that are common
print(strings)
coun.discard("Peru")  # deletes Peru from set coun
print(coun)
x={"India","Iran","Dubai"}
a=x.intersection(coun)  # returns a set of common elements
print(a)
x.intersection_update(coun) # removes uncommon items from x
print(x)
print("coun: ",coun)
print("strings: ",strings)
b= coun.isdisjoint(strings) # returns True if no common items are present in coun & strings
print("coun and string is disjoint: ",b)
u={"a","b","c"}
v={"b","c","d","e","f"}
print("u is subset of v: ",u.issubset(v)) # returns true if u is present in v but "a" is not present in v so false
v.add("a") # "a" added to v
print("v is superset of u: ",v.issuperset(u)) # prints true bcz all elements of u are in v
coun.pop()  # removes random element
print(coun)
strings.remove("hii")  # removes "hii"
print(strings)
# returns set with only uncommon elements
print("u & v without common elements: ",u.symmetric_difference(v))   
#removes common items and also inserts those that are not present in both
u.symmetric_difference_update(v)
print(u)
n1={1,2,3,4}
n2={5,6,7}
n3={8,9,10,}
print("The union of n1, n2 & n3 = ", n1.union(n2,n3))
n1.update(n2) # Inserts thems from n2 into n1
print(n1) 