#022.Write a program to find duplicate elements in a tuple.

t = (1, 2, 3, 2, 4, 1, 5)
d={}
i=0
while(i<len(t)):
    if t[i] in d:
        d[t[i]]+=1
    else:
        d[t[i]]=1
    i+=1
print(d)
for key,value in d.items():  
    if value>1:
        print(key)
