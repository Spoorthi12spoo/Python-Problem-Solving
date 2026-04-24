#033.Sum of each sublist
#Return [6, 9, 6] for [[1,2,3],[4,5],[6]]

l=[[1,2,3],[4,5],[6]]
l1=[]
for i in l:
    total=0
    for j in i:
        total+=j
    l1+=[total]
print(l1)

res=[sum(sublist) for sublist in l]
print(res)

#recusion method for deeper level bcz loops work only for one level of nesting
l = [[1, [2, 3]], [4, [5, 6]]]

def sum_each_main(l):
    res=[]
    for i in l:
        res.append(sum_each_sublist(i))
    return res

def sum_each_sublist(sub_list):
   total=0
   for i in sub_list:
       if isinstance(i,list):
           total+=sum_each_sublist(i)
       else:
           total+=i
          
   return total
print(sum_each_main(l))
