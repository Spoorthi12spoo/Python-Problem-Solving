#031.Delete multiple keys from a dictionary.
#Example: Remove ("a","c") from dictionary.

D={'a':3,'b':2,'c':1}
t=tuple(input("enter the key you wanted to delete"))
for key in D:
    if key in t:
        del D[key]
print(D)
