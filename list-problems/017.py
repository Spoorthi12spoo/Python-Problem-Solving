#017.Remove all occurrences of a specific element from a list.

l=list(map(int,input().split()))
l1=[]
E=int(input("enter an element you wanted to remove: "))
i=0
while(i<len(l)):
    if l[i]==E:    #instead  if l[i]!=E:
        l1+=l[i]                #l1+=[]
    else:
        l1+=[l[i]]
    i+=1
print(l1)
