#045. Find the key associated with a given value.
#Example: find key for value 'b'.

D={1:'a',2:'b',3:'c'}
for key,value in D.items():
    if value=='b':
        print(key)
