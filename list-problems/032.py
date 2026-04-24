#032.	Find maximum and minimum element in a nested list.
# [[3, 5], [7, 2, 9], [4]] → max = 9, min = 2

l=[[3, 5], [7, 2, 9], [4]] 
maximum=float('-inf')
minimum=float('inf')
def max_min(l):
    global maximum,minimum
    for i in l:
        if isinstance(i,list):
           max_min(i)
        else:
            if i>maximum:
                maximum=i
            if i<minimum:
               minimum=i
    return maximum,minimum
print(max_min(l))
