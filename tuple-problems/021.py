#021.Convert a tuple of tuples to a dictionary (e.g., ((1,'a'), (2,'b')) → {1:'a', 2:'b'}).

t=((1,'a'),(2,'b'))
d={}
for key,value in t:
        d[key]=value
print(d)
