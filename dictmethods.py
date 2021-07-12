animals={
    "Cow":"Herbivore",
    "Lion":"Carnivore",
    "Man":"Omnivore"
}
print("animals: ", animals)
x=animals.copy() # copied the dictionary items in x
print("After copy()...x: ",x)

y=animals.get("Cow")  # Gets value of "Cow" item
print("Using get(): ",y)

print("Using items(): ",animals.items()) # Returns a view object containing the key-value pairs of the dict

print("Using keys(): ",animals.keys()) # Returns a view object containing the keys of the dict

print("Using values(): ",animals.values()) # Returns a view object containing the values of the dict

m=animals.pop("Man") # Removes Man from the dict and the value of Man is stored in m
print("After pop() animals: ",animals)
print("pop() returned: ",m)

animals.clear() # Removed all the elements from animals
print("After clear()...animals: ",animals)

a=("1","2","3") #keys of mydict
b=5
mydict= dict.fromkeys(a,b)  # creating a dictionary with 3 keys all with value 5
print("Using fromkeys(): ",mydict)

x= mydict.setdefault("2","6")  # Returns value of the item with specified key
print("Value of 2: ",x)
print("Value of 4(which is not in mydict): ",mydict.setdefault("4","12")) # Inserts key 4 with value 12
print(mydict)

print("Using popitems(): ", mydict.popitem())  # Removes the last item. Returns a tuple

mydict.update({"4":"6","5":"8"}) # Inserts two key-value pair
print("After using update()",mydict)