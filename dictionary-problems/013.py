#013 Convert a list of tuples into a dictionary using comprehension.
#Example: [(1,'a'),(2,'b')] → {1:'a',2:'b'}

l_t=[(1,'a'),(2,'b')]
d={key:value for key,value in l_t}
print(d)

D={}
for key,value in l_t:
    D[key]=value
print(D)
