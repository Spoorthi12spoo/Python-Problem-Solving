#004.	Create a tuple and print it in reverse order.

my_tuple=(1,2,3,4,5,"spoo","sne")
print(my_tuple[::-1])

for i in range(len(my_tuple)-1,-1,-1):
    print(my_tuple[i],end=" ")
rev_tuple=tuple(reversed(my_tuple))
print(rev_tuple)


rev=()
for i in t:
    rev=(i,)+rev
print(rev)
