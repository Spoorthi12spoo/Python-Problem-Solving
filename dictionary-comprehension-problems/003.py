#003.	Convert a list of numbers [1,2,3,4] into a dictionary where each number is a key and its cube is the value.

l=[1,2,3,4]
cube={num:num**3 for num in l}
print((cube))
