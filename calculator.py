print("Enter + for addition, - for substraction, * for multiplication / for division")
ch=input()
if ch=="+":
    sum=0
    n=int(input("Enter how many no.s do u want to add: "))
    l=[]
    print("Enter the nos. one by one")
    for i in range(n):
        x=int(input("Enter: "))
        l.append(x)
    for i in range(n):
        sum=sum+ l[i]
    print("Sum of the numbers= ",sum)
elif ch=="-":
    a=int(input("Enter 1st number from which 2nd number is to be subtracted: "))
    b=int(input("Enter 2nd number that is to be subtracted from the 1st    : "))
    print("a-b = ",(a-b))
elif ch=="*":
    mul=1
    n=int(input("Enter how many no.s do u want to multiply: "))
    l=[]
    print("Enter the nos. one by one")
    for i in range(n):
        x=int(input("Enter: "))
        l.append(x)
    for i in range(n):
        mul=mul* l[i]
    print("Product of the numbers= ",mul)
elif ch=="/":
    a=int(input("Enter 1st number(dividend): "))
    b=int(input("Enter 2nd number(divisor) : "))
    print("a/b = ",(a/b))
else:
    print("Enter correct symbol")
