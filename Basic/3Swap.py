#method 1
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
temp=a
a=b
b=temp
print("Value of a after swapping:",a)
print("Value of b after swapping:",b)

#method 2
c=int(input("Enter the value of c:"))
d=int(input("Enter the value of d:"))
c,d= d,c
print("value of c after swapping:",c)
print("value of d after swapping:",d)

