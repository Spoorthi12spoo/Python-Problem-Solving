#009.	Write a program to find the index of an element in a tuple.

t=(1,2,3,4,20)
E=int(input("enter an element you wanted to find index: "))
for i in range(len(t)):
    if t[i]==E:
        print(i)
        break
else:
    print("element not exists")

#or
print(t.index(E))
