#010.Find the average of all numbers in a list.

l=list(map(int,input().split()))
i=0
total=0
num=0
while(i<len(l)):
    total+=l[i]
    num+=1
    i+=1
avg=total/num
print(avg)
