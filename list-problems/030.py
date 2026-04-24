#030.Access specific elements
#Example: print 4th element (using both indexing and loops).

l = [[1, 2], [3, 4, 5], [6, 7]]
print(l[1][1])      #using indexing

count=0
for sublist in l:
    for item in sublist:
        count+=1
        if count==4:
            print(item)         #using looping
