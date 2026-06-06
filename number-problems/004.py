#004.fibanacci series using iterative method and recursive methods

#iterative
num=int(input())
a,b=0,1
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b

#another easiest way

a=0
b=1
n=6
print(a)
print(b)
for i in range(n-2):
    a,b=b,a+b
    print(b)


#recurive

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
num=int(input("enter a number: "))
for i in range(num):
    print(fib(i),end=" ")
