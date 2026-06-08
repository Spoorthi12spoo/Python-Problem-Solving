#028.Extract only even values from a dictionary.
#Example: {1:4, 2:5, 3:6} → [4,6]

D={1:4, 2:5, 3:6}
even=[]
for value in D.values():
    if value%2==0:
        even+=[value] #or even.append(value)
print(even)
