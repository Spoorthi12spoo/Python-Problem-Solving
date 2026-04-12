#014. Find unique elements that appear only once in a list.

l1=[1,2,3,3,4,4,5,1]
D={}
for i in l1:
    if i in D:
        D[i]+=1
    else:
        D[i]=1
unique=[]
for key in D:
    if D[key]==1:
        unique+=[key]
print(unique)
