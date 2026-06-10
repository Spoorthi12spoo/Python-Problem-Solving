#039.Convert dictionary into a list of key–value tuples.
#Example: {1:'a',2:'b'} → [(1,'a'),(2,'b')]

D={1:'a',2:'b'} 
l=[]
for i in D.items():
    l+=[i]     #or l.append(i)   
print(l)

#or
D={1:'a',2:'b'} 
res=list(D.items())
print(res)
