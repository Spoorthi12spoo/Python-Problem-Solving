#019.Convert two lists (keys list & values list) into a dictionary.

keys=['a','b','c','d']
values=[1,2,3,4]
dic={}
for i in range(len(keys)):
        dic[keys[i]]=values[i]
print(dic)

keys = ['name', 'age', 'city']    #another example
values = ['John', 25, 'Bengaluru']
D={}
for i in range(len(keys)):
        D[keys[i]]=values[i]
print(D)

print(dict(zip(keys,values)))    #another method
