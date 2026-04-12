#016.Replace all occurrences of a specific element with another value.

l1=[2,2,3,3,4,4,5]
l2=[]
old=int(input("enter an element you wanted to replace"))
new=int(input("enter new value: "))
for i in l1:
    if i==old:
        i=new
    l2+=[i]
print(l2)
