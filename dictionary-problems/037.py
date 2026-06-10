#037. Find keys with duplicate values.
#Example: {1:'a',2:'b',3:'a'} → 'a' occurs twice'

D = {1:'a', 2:'b', 3:'a'}
values = list(D.values())

duplicate = False
max_count = 0

for i in range(len(values)):
    count = 1
    for j in range(i + 1, len(values)):
        if values[i] == values[j]:
            duplicate = True
            count += 1

    if count > max_count:
        max_count = count
        dup_val = values[i]

if duplicate and max_count > 1:
    print(f"{dup_val} appears {max_count} times")
else:
    print("no duplicates")

#another method

D = {1:'a', 2:'b', 3:'a'}
values = list(D.values())
counts={}
for value in values:
    if value not in counts:
        counts[value]=1
    else:
        counts[value]+=1
duplicate=False
for k,c in counts.items():
    if c>1:
        print(f"{k} appears {c} times")
        duplicate=True
if not duplicate:
        print("no duplicates")
