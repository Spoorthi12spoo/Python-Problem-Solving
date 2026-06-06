#027 Count how many integers are present

t = (1, (2, 3), ("a", (4, 5)))
def count_integer(t):
    i=0
    count=0
    while(i<len(t)):
   
        if isinstance(t[i],tuple):
            count+=count_integer(t[i])
        elif isinstance(t[i],int):
            count+=1
        i+=1
    return count
print(count_integer(t))
