#038.Reverse only the order of values in a dictionary.
#Example: {1:'x',2:'y',3:'z'} → {1:'z',2:'y',3:'x'}

D1={1:'x',2:'y',3:'z'}
D2={}
values=list(D1.values())
rev_values=[]

for i in range(len(values)-1,-1,-1):
        rev_values+=values[i]
i=0
for key in D1.keys():
        D2[key]=rev_values[i]
        i+=1
print(D2)
