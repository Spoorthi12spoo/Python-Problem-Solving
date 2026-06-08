#022. Remove all duplicate values from a dictionary.

D = {1:'a', 2:'b', 3:'a', 4:'c'}
unique={}
values=[]
for k,v in D.items():
    if v not in values:
        unique[k]=v
        values.append(v)
print(unique)
