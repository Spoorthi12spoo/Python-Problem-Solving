#3.	Count total elements in a nested list.
# Count every number at all depths.


l = [[1,[2,[3,[4]]]]]
def count_elements(lst):
    count=0
    for i in lst:
         if isinstance(i,list):
            count+=count_elements(i)
         else:
            count+=1
       
    return count
print(count_elements(l))

#or  
while(i<len(lst)):
  if isinstance(lst[i],list):
    count+=count_elements(lst[i])
