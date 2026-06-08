#012.Create a dictionary using comprehension where keys are numbers 1–10 and values are cubes.

D={i:i**3 for i in range(1,11)}
print(D)

D={}
for i in range(1,11):
    D[i]=i**3
print(D)
