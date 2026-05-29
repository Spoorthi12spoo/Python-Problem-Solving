#010.Count how many times a particular element appears in a tuple.

t=(1,1,2,2,3,3,3,3,4)
count=0
E=2
for item in t:
    if item==E:
        count+=1
print(count)

#or
print(t.count(E))
