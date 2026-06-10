#006.	Filter a dictionary {1: 'one', 2:'two', 3:'three'} to keep only items where the key is even.

D={1: 'one', 2:'two', 3:'three',4:'four'}
even={key:value for key,value in D.items() if key%2==0}
print(even)
