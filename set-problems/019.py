#019.Return the maximum and minimum element from a set.

A={1,2,3,4}
max=1         #or max=None
for i in A:
    if i>max:    #if max is None or i>max:(same follows for min)
        max=i
print(max)


A={1,2,3,4}
min=1
for i in A:
    if i<min:
        min=i
print(min)

#or

A = {1, 2, 3, 4}

# Initialize max and min safely
max_val = min_val = next(iter(A))  # take first element from set

for i in A:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum:", max_val)
print("Minimum:", min_val)
