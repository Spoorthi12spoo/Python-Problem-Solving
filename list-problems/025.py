#025.Rotate a list to the right by k positions.

l = [1,2,3,4,5]
k = 2
k = k % len(l)           # safe for large k
rotated = l[-k:] + l[:-k]
print(rotated)    
