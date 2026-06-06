#024.Write a program in Python to find prime factors of a given integer.

num = int(input("Enter a number: "))
i = 2
while i <= num:
    if num % i == 0:
        print(i, end=" ")
        num //= i
    else:
        i += 1
