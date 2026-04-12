#013.Find common elements between two lists.

l1=[1,2,3,4,5]
l2=[6,7,1,2,3]
common=[]
for i in l1:
    if i in l2:
        common+=[i]
print(common)
