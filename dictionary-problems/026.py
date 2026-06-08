#026.Remove all keys that have None values from a dictionary.
#Example:{'a': 1, 'b': None, 'c': 3} → {'a':1,'c':3}

D={'a': 1, 'b': None, 'c': 3} 
D1={}
for i in D:
    if D[i] is not None:   #   if D[i]!=None:
        D1[i]=D[i]
print(D1)
