#018.Sort dictionary by values.

#sorting values
D = {'d': 1, 'b': 2, 'c': 3}
items=list(D.items())
for i in range(len(items)):
    for j in range(0,len(items)-i-1):
        if items[j][1]>items[j+1][1]:
            items[j],items[j+1]=items[j+1],items[j]
sorted_dict=dict(items)
print(sorted_dict)  
