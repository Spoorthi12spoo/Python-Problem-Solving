#006.Check if a particular element exists in the list.

l=input().split()  #if you want for integer list(map(int,input().split()))
no=input("enter an element you wanted to check")  #or int(input())
i=0
while(i<len(l)):
    if no==l[i]:
        print("the given no is exist")
        break
    i=i+1
else:
    print("not exist")
