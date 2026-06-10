#010.Invert a dictionary {‘a’:1, ‘b’:2, ‘c’:3} to {1:'a', 2:'b', 3:'c'}.

D={'a':1, 'b':2, 'c':3} 
inverse={value:key for key,value in D.items()}
print(inverse)
