#030 Find the depth of a nested tuple

t = (1, (2, (3, (4, 5))))  #wrong
def depth_tuple(t):
    count=0
    for i in t:
        if isinstance(i,tuple):
            count=depth_tuple(i)

    return count
print(depth_tuple(t))
