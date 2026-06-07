#022.Given two sets, remove the common elements from both.(Mutual elimination)

A={1,2,3}
B={4,5,2,6}
common=A & B
for x in common:
    A.remove(x)
    B.remove(x)
print(A,B)
