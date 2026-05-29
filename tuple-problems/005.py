#005.Check whether an element exists in a tuple or not.

t=(1,2,3,4,5)
E=int(input("enter an element you wanted to check: "))
if E in t:
    print("element exists")
else:
    print("element not exists")

found=False
for i in t:
    if i==E:
        found=True
        break
if found:
    print("element exists")
else:
    print("element not exists")
