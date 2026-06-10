#015.Given a string "mississippi", create a dictionary with characters as keys and True if the character appears more than once, else False.

str="mississippi"
D={ch:True if str.count(ch)>1 else False for ch in str}
print(D)
