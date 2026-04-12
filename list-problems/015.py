#015.Sort a list without using the sort() or sorted() function.

l1 = [5, 3, 8, 4, 2]

n = len(l1)

for i in range(n):
    for j in range(0, n - i - 1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]   # Direct swap

print("Sorted list:", l1)

#Using the sort() or sorted() function.
print(l1)
l2=l1.sort()
print(l2)
l2=sorted(l1)
print(l2)
