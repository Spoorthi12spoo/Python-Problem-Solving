#002.	Given a list ['a','b','c'] and a list [1,2,3], create a dictionary mapping each letter to its corresponding number.

letters=['a','b','c']
numbers=[1,2,3]
D={letters[i]:numbers[i] for i  in range(len(letters))}
print(D)
