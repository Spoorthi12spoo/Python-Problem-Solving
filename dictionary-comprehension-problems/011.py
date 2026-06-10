#011.Given a list of words ["apple","banana","cherry"], create a dictionary with word lengths.

fruits=["apple","banana","cherry"]
D={fru:len(fru) for fru in fruits}
print(D)
