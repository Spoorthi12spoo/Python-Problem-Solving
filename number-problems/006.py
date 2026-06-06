#006.Write a program in Python to check if a number is binary

num=int(input("enter a number: "))
while(num>0):
    bin=num%10
    if bin!=0 and bin!=1:
        print("number is not binary")
        break
    num//=10
    if num==0:
        print("number is binary")
