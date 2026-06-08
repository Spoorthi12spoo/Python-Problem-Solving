#017.Sort a dictionary by keys in ascending and descending order.

#sorting keys
D={'d':1,'b':2,'c':3}
keys=list(D.keys())
for i in range(len(keys)):
    for j in range(0,len(keys)-i-1):
        if keys[j]>keys[j+1]:
            keys[j],keys[j+1]=keys[j+1],keys[j]
sorted_dict={}
for key in keys:
    sorted_dict[key]=D[key]
print(sorted_dict)

sorted_dict_asc=dict(sorted(D.items()))
print(sorted_dict_asc)
