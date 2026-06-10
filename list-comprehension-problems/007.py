#007.	Flatten a 2D list [[1,2],[3,4],[5,6]] into [1,2,3,4,5,6] using list comprehension.

L=[[1,2],[3,4],[5,6]] 
flatten=[num1 for num in L for num1 in num]
print(flatten)
