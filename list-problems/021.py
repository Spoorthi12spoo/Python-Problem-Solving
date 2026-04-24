#021.Create a new list containing the square of each number from another list.

l1=[2,3,4,5,6]
l2=[]
for i in l1:
    l2+= [i**2]   #or l2.append(i**2)  
print(l2)
