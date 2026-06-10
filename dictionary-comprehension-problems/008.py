#008.	Create a dictionary where keys are numbers 1 to 10 and values are "even" or "odd" depending on the number.

D={key:"even" if key%2==0 else "Odd"for key in range(1,11)}
print(D)
