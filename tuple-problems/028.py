#028 Sum of all numeric elements

t = (1, (2, 3), ("a", (4, "x"), 5))
def sum_elements(t1):
    total=0
    for i in t1:
        if isinstance(i,tuple):
            total+=sum_elements(i)
        elif isinstance(i,(int,float)):
            total+=i
    return total
print(sum_elements(t))
