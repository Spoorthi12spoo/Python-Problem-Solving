#009.	Given two lists ['x','y','z'] and [9,8,7], create a dictionary using dictionary comprehension.

l1=['x','y','z'] 
l2=[9,8,7]
D={key:value for key,value in zip(l1,l2)}
print(D)

#or D={l1[i]:l2[i] for i in range(len(l1))}
