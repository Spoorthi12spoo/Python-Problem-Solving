#014. Count frequency of each character in a string using a dictionary.
s = "hello"
D={}
for i in s:
    if i in D:
        D[i]+=1
    else:
        D[i]=1
print(D)

#or
s = "hello"
D={}
for ch in s:
    D[ch]=D.get(ch,0)+1
print(D)
