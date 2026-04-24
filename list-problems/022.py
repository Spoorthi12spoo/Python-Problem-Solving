#022.Print all elements of a list in reverse order using a loop.

l1=[1,3,4,5,6]
rev=[]
for i in l1:
    rev=[i]+rev    #or rev.append(i)
print(rev)
