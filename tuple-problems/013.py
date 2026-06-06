#013.Slice a tuple from index 2 to 5 and print it

t=("apple","banana","cherry","mango","orange","grapes")
res=t[2:5]
print(res)

result=()
for i in range(2,5):
    result+=(t[i],)
print(result)
