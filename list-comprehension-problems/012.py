#012.Remove all vowels from a string "hello world" using list comprehension.

S="hello world"
vowels='aeiou'
L=[ch for ch in S if ch.lower() not in vowels ]   #or result = "".join([ch for ch in s if ch not in vowels])
print("".join(L))
