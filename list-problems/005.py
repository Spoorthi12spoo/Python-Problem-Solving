#005.Count how many times a given element appears in a list.

l=list(map(int,input().split()))
no=int(input())
count=0
for i in l:
    if i==no:
        count+=1
print(f"{no} appears {count} times")
