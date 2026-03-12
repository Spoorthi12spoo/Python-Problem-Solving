#3.Find the smallest number in a list without using min().

l=[2,3,4,5,1]
if l:
    min_no=l[0]
    for i in l:
        if i<min_no:
            min_no=i
    print(min_no)
else:
    print("list is empty")

#or
print(min(l))
