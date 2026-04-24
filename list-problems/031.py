#031.Flatten a nested list
#Convert [[1, 2], [3, 4], [5, 6]] to [1, 2, 3, 4, 5, 6]

l=[[1, 2], [3, 4], [5, 6]]
l1=[] 
for i in l:
    for j in i:
        l1+=[j]
print(l1)

#recursive method
l = [[1,[2,[3,[4]]]]]

def nested_list(l):
    l1=[]
    for i in l:
        if isinstance(i,list):
            l1+=nested_list(i)
        else:
            l1+=[i]
    return l1
print(nested_list(l))
