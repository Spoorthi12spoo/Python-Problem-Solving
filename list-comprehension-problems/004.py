#004.	Create a list of cubes of even numbers between 1 and 10.

cubes=[num**3 for num in range(1,11) if num%2==0]
print(cubes)
