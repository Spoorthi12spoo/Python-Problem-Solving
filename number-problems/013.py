#013.Python Program to calculate the power without using POW function.(using while loop).

base=int(input("enter the base: "))
exponent=int(input("enter the exponent:" ))
result=1
i=0
while(i<exponent):
    result=result*base
    i=i+1
print(result)
