#007.Remove duplicate elements from a list.

l1=input().split()
l2=[]
i=0
while i<len(l1):
    if l1[i] not in l2:
        l2+=l1[i]
    i+=1
print(l2)
