#026.Python program to calculate sum of integers in string.

integers="123"
total=0
for i in integers:
    if i.isdigit():
        total+=int(i)
print(total)
