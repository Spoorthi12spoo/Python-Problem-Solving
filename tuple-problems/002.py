#002.	How do you access the 3rd element from a tuple?

t=(1,2,3,5,6)
count=0
for i in t:
    count+=1
    if count==3:
        print(i)
print(t[2])
