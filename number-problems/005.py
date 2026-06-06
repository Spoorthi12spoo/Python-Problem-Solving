#005.Write a program in Python to find greatest among three integers.

a,b,c=map(int,input("enter three numbers: ").split())
if (a>b) and (a>c):
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")
