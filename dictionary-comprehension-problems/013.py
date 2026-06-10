#013.Create a dictionary of numbers 1 to 10 with values being their factorial.

#using built in
import math
factorial={i:math.factorial(i) for i in range(1,11)}
print(factorial)

#without built-in
def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

fact={i:factorial(i) for i in range(1,11)}
print(fact)
