#005.Create a dictionary from a string "hello" where keys are characters and values are their frequency counts.

str="hello"
D={ch:str.count(ch)for ch in str}
print(D)
