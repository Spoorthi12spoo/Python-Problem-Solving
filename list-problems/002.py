#2.Find the largest number in a list without using max().

l=[7,8,9,10,15,4]
if l:           
    max_no=l[0]
    for i in l:
        if i>max_no:
            max_no=i
    print(max_no)
else:
    print("list is empty")

#or

print(max(l))
