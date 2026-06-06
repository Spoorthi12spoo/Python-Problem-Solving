#026 Print only numeric values

def numeric(t):
    res = ()
    for i in t:
        if isinstance(i, tuple):
            res += numeric(i)
        elif isinstance(i, (int, float)):
            res += (i,)
    return res

t = (1, "a", (2, 3), ("x", (4, "y")))
print(numeric(t))
