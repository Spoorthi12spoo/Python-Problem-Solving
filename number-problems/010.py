#010.Write a program in Python to add two integer without using arithmetic operator.

x=int(input("enter a number"))
y=int(input("enter a number:"))
while(y!=0):
    carry=x & y
    x=x^y
    y=carry<<1
print(x)
