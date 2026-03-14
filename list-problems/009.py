#009.Separate even and odd numbers from a list into two different lists.

l=list(map(int,input().split()))
even=[]
odd=[]
for i in l:
    if i%2==0:
        even+=[i]
    else:
        odd+=[i]
print(even,odd)
