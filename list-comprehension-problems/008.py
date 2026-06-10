#008.Given a list of strings ["apple", "banana", "cherry"], create a list of the lengths of each string.

L=["apple", "banana", "cherry"]

l_Length=[len(fru) for fru in L ]  #or lengths = [sum(1 for _ in word) for word in fruits] 
print(l_Length)
