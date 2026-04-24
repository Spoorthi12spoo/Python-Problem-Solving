#019.Find the index of the first and last occurrence of an element.

l=[1,2,3,4,5,3,3,8,9,10]
E=int(input("enter an element you wanted to find first and last index."))
first=-1
last=-1

for i in range(len(l)):
    if l[i]==E:
        if first==-1:
            first=i
        last=i
if first == -1:
    print("Element not found")
else:
    print(f"{E} found at first position {first} and last position {last}")
