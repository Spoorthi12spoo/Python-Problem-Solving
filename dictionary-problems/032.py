#032.Convert dictionary keys into a list and values into another list.
#Example: {1:'x', 2:'y'} → [1,2] and ['x','y']

D={1:'x', 2:'y'}
keys=[]
values=[]
for i in D:
    keys+=[i]
    values+=D[i]
print(keys,values)
