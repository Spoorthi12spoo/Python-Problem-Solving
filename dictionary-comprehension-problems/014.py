#014.Given {'x':1,'y':2,'z':3}, create a dictionary where values are squared.

D={'x':1,'y':2,'z':3}
square={key:value**2 for key,value in D.items()}
print(square)
