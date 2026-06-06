#015.Check whether two tuples are equal or not.

t1=tuple(map(int,input().split()))  # == operator compares both length and each element’s position & value.
t2=tuple(map(int,input().split()))  #t1 = (1, 2, 3)
                                    #t2 = (3, 2, 1)  t1==t2 false because position is different
if t1==t2:
    print("two tuples are equal")
else:
    print("not equal")
