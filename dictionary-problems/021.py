#21.Invert a dictionary (swap keys and values).
#Example: {1:'a', 2:'b'} → {'a':1, 'b':2}

D={1:'a', 2:'b'} 
D1={}
for key,value in D.items():
    D1[value]=key
   
print(D1)

#using dictionary comprehension
D={1:'a', 2:'b'} 
inverted={v:k for k,v in D.items()}
print(inverted)
