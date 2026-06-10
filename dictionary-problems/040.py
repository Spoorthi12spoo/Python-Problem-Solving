#040.Create dictionary from list but skip duplicates in list.
#Example:
#List: [1,2,2,3]
#Dict: {1:0,2:1,3:3} (value = index of first occurrence)

List=[1,2,2,3]
D={}
for i in range(len(List)):
    if List[i] not in D:
        D[List[i]]=i
print(D)

#or
lst = [1, 2, 2, 3]
D = {}

for idx, val in enumerate(lst):
    if val not in D:
        D[val] = idx

print(D)
