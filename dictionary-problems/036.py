#036.Create a dictionary from two lists but only pair values that are at even indexes.
#Example: Keys = [‘a’, ‘b’, ‘c’, ‘d’] Values = [1,2,3,4] Output → {‘a’:1, ‘c’:3}

Keys = ['a', 'b', 'c', 'd'] 
Values = [1,2,3,4]
res={}
for i in range(0,min(len(Keys),len(Values)),2):
    res[Keys[i]]=Values[i] 
print(res)
