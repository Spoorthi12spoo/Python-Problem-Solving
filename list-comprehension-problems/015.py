#015.Given a list of numbers [1,2,3,4,5], create a list where each number is squared if it is even, else cubed.

l=[1,2,3,4,5]
L1=[num**2 if num%2==0 else num**3 for num in l]
print(L1)
