#024.Find the difference between two lists (elements in one list but not in the other).

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
unique=[]
for i in list1:
    if i not in list2:
        unique+=[i]   #unique.append(i)
print(unique)

diff=list(set(list1)-set(list2))
print(diff)
