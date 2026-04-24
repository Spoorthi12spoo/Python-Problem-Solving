#020.Remove all empty lists or empty strings from a list.

l=["abc"," ",[],"xyz"]
l1=[]
for i in l:
    if i!=" " and i!=[]:   
        l1+=[i]                          
print(l1)
