coun=["India","USA","England"]
coun.append("Peru") # adds Peru at the end of the list-coun
print(coun)
x= coun.copy()  #returns copy of the list coun
print(x)
num=[1,2,3,5,2,6,1,4,1]
print(num.count(1))  #count(1) counts the no. of times 1 occurs
x.clear() # removes all elements from the list x but list exists
print(x)  
strings=["Hello","hii","hurray"] 
coun.extend(strings) # adds the elements of strings to the end of coun
print(coun) 
a=strings.index("hii")  # returns the index of hii in the list
print(a)
strings.insert(2,"welcome") # inserts welcome as 3rd element of strings list
print(strings)
strings.pop(3)  # removes 4th element in strings(hurray)
print(strings)
coun.remove("England")  # removes England fron coun list
print(coun)
num.sort() # arranges list in ascending order
print(num)
num.reverse() # reverses the list i.e., in descending order
print(num)