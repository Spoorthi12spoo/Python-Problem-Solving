#004.Reverse a list without using the reverse() function.

l=[2,3,4,5,1]
rev=[]
for i in l:
    rev=[i]+rev
print(rev)
