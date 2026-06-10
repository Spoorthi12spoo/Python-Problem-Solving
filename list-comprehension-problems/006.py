#006.	Filter a list of numbers [10, 15, 20, 25, 30] to include only numbers divisible by 3.

L=[10, 15, 20, 25, 30]
mul3=[num for num in L  if num%3==0]
print(mul3)
