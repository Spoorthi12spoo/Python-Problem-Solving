#027.Find the sum of all values in a dictionary.
#Example: { 'a': 10, 'b': 20 } → 30

D={ 'a': 10, 'b': 20 }
total=0
for value in D.values():
    total+=value
print(total)
