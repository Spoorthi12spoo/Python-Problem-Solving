#023.Find the element-wise sum of two tuples of the same length.

t1=(2,3,4)
t2=(4,5,6)
res=()
for i in range(len(t1)):
    res+=(t1[i]+t2[i],)
print(res)


#(t1[i] + t2[i],) creates a 1-element tuple, like (6,)
#Then res += (6,) concatenates this single-element tuple to your existing tuple.
