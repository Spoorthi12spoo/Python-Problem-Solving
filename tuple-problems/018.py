#018.Write a program to sort a tuple of numbers in ascending order (convert to list if needed).

t=(1,2,3,4,7,6,5)
t1=list(t)
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t1[j]<t1[i]:
            t1[j],t1[i]=t1[i],t1[j]
print(tuple(t1))

t1.sort()
print(t1)
print(sorted(t))  #it returns a list, not a tuple.

#you can’t directly use sort() or sorted() to modify a tuple without converting into list,
#but you can use sorted() to get a sorted version of it.
