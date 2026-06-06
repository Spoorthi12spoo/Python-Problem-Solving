#020.Write a program to find the sum of all numeric elements in a tuple.

t=(1,2,3,4,4)
total=0
for i in t:
    total+=i
print(total)

print(sum(t))
