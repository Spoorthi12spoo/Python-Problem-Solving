#011.Concatenate two tuples and print the result.

t1=(1,2,3,4)
t2=(5,6,7,8)
res=t1+t2
print(res)

result = sum((t1, t2), ())
print(result)
