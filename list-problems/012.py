#012.Merge two lists without using the + operator.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merge_list=[0]*(len(list1)+len(list2))
index=0
for sublist in(list1,list2):
    for item in sublist:
        merge_list[index]=item
        index+=1
print(merge_list)
