#030.Write a program to find common keys in two dictionaries.
#Example:D1={"a":1,"b":2}  D2={"b":3,"c":4} → ['b']

D1={"a":1,"b":2}
D2={"b":3,"a":4} 
res=[]
for key in D1.keys():
    if key in D2:  
        res+=key    
print(res)
