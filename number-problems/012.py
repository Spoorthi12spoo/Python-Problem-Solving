#012.Python Program to calculate the power without using POW function.(using for loop).

base=int(input("enter the base: "))
exponent=int(input(input("enter the exponent:" )))
result=1
for i in range(exponent):
    result=result*base
print(result)
