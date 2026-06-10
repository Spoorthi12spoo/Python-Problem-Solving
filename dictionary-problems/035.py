#035.Write a program to multiply all values in a dictionary.
#Example: {1: 2, 2: 3, 3: 4} → 24

D={1: 2, 2: 3, 3: 4}
mul=1
for i in D.values():
    mul*=i
print(mul)
