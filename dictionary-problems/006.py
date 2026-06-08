#006. Replace all values in a dictionary with their squares.
D= {1: 2, 2: 3} 
for i in D:
    D[i]=D[i]**2
print(D)

D={key:value**2 for key,value in D.items()}   #using dictionary comprehension
print(D)
