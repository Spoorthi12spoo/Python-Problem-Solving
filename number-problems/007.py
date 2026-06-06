#007.Write a program in Python to find sum of digits of a number using recursion?

number=int(input())
sum=0
for i in str(number):
    sum+=int(i)
print(sum)


def sum(num):
    if num==0:
        return 0
    else:
        return num%10+sum(num//10)
    
num=int(input())
print(sum(num))
