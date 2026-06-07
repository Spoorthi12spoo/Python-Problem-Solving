#015. Convert a list of lists into a set of tuples.
#(Because sets cannot hold lists — mutable)
#L = [[1, 2], [3, 4], [1, 2]]   Output :{(1, 2), (3, 4)}

L = [[1, 2], [3, 4], [1, 2]]
S=set()
for i in L:
    S.add(tuple(i))   
print(S)

#or

L = [[1, 2], [3, 4], [1, 2]]
result = set(tuple(x) for x in L)
print(result)

#why tuple conversion?
#because set stores only immutable values,list is mutable so we need to convert into tuple.
