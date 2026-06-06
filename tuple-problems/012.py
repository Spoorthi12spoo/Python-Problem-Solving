#012.Repeat a tuple three times using the * operator.

t=(1,2,3,4,5)
res=t*3
print(res)

#without *
t = (1, 2, 3, 4, 5)
res = ()
for i in range(3):
    res += t
print(res)
