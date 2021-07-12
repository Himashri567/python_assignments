txt= "hii everyone, my name is Himashri Basu"
x=txt.capitalize() # converts the 1st letter of the sentence to uppercase and all other characters are in lower case
print("After using capitalize(): ", x) 

print("name is present at location: ",txt.find("name"))

txt="Hello! How Are You Doing"
print("All words start with capital letter: ",txt.istitle())

print("After using casefold(): ", txt.casefold()) # Converts lettes to lower case

txt="Hello World!"
print(txt.center(30,'*')) # The text will be center aligned * will be filled in empty space by default which is space

print("Where in the text is the 1st occurrence of 'o': ",txt.index("o"))

print(txt.encode())

print("The line ends with !: ",txt.endswith("!")) # Returns true because the sentences ends with the given parameter- !

print("All chars in '",txt,"' are in lower case: ", txt.islower())

print("The line starts with H: ",txt.startswith("H")) # Returns true because the sentences starts with the given parameter-H

a="Buy this for rupees: {price: .2f} !"
print(a.format(price = 100))

txt="1-2-3 Go"
print("The text ",txt," is alphanumeric: ",txt.isalpha()) # - is alphanumeric character

a="\u0033" # unicode for 3
b="\u0047" # unicode for G
print("0 is decimal number", a.isdecimal())
print("G is decimal number", b.isdecimal())

a="1234"
print("All chars in ",a," are digits: ",a.isdigit())

print("All chars in ",a," are numerics: ",a.isnumeric())

txt = "H\ti\tm\ta\tshri"
x =  txt.expandtabs(2)
print("After Setting the tab size to 2 whitespaces: ",x)

a = "Python"
b = "Prog 12" # space- wrong
c = "11donealready" # starts with digit - wrong
print("Python is a valid identifier: ",a.isidentifier())
print("Prog12 is a valid identifier: ",b.isidentifier())
print("2bring is a valid identifier: ",c.isidentifier())

txt = "Hello!\n  How are you?"
print("The sentence is printable: ",txt.isprintable()) # \n cannot be printed

x = txt.splitlines()
print("After using splitlines(): ",x)

txt = "   "
print("All characters are spaces in ",txt , txt.isspace())

a=("1","2","3")
txt= " joined "
print(txt.join(a))

txt = "I am"
x = txt.ljust(10) # left justified
print(x, "Himashri Basu")

x = txt.rjust(10) # right justified
print(x, "Himashri Basu")