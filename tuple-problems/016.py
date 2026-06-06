#016.Unpack a tuple into separate variables and print each variable.


t=tuple(map(int,input().split())) 
#a,b,c=t
#print(a,b,c ,sep="\n")

print(*t,sep="\n")
