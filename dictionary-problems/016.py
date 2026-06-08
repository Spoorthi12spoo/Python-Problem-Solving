#016.Find the key with the maximum value in a dictionary.

D={'a':1,'b':2,'c':3}
maximum=D['a']
for i in D:
    if D[i]>maximum:
        maximum=D[i]
print(maximum)

max_val=max(D,key=D.get)   #it only fetches key
print(D[max_val])          #to fetch value
