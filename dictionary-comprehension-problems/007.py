#007.	Given {'a':1,'b':2,'c':3}, create a new dictionary with values doubled.

D={'a':1,'b':2,'c':3}
double={key:value*2 for key,value in D.items()}
print(double)
