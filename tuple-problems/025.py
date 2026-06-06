#025 Flatten a nested tuple
t = (1, (2, 3), (4, (5, 6)))

def flatten_tuple(t):
    res=()
    for i in t:
        if isinstance(i,tuple):
            res+=flatten_tuple(i)
        else:
            res+=(i,)
    return res
print(flatten_tuple(t))
