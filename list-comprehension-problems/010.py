#010.Create a list of numbers from 1 to 20, but replace multiples of 3 with the string "Fizz".

L=["Fizz" if num%3==0 else num for num in range(1,21) ]
print(L)
