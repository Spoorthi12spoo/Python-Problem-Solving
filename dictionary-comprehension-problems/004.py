#004.	Swap keys and values in a dictionary {1:'a', 2:'b', 3:'c'}.
D={1:'a', 2:'b', 3:'c',4:'c'}
 
swap={value:key for key,value in D.items()}   #it works only if values are unique
print(swap)
