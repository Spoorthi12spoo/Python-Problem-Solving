#009.	Convert all strings in a list ["a", "b", "c"] to uppercase using list comprehension.

L=["a", "b", "c"]
upper=[chr(ord(ch)-32) for ch in L]   #You could also use Python’s built-in upper() method:
print(upper)
