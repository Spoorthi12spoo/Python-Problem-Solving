#028.	Find the sum of all numbers in a nested list.

[[1, 2, 3], [4, 5], [6]] → 21
l=[[1, 2, 3], [4, 5], [6]]
total=0
for i in l:
    for j in i:
        total+=j
print(total)
