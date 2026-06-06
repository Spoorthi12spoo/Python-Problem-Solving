#024.Write a program to remove duplicates from a tuple and return a new tuple.

t = (1, 2, 3, 4, 5, 2, 3)
new_t = ()

for i in t:
    if i not in new_t:
        new_t += (i,)
print(new_t)
