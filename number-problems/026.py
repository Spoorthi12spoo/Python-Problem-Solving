#026.Python program to print first n Prime Number with explanation.

n = int(input("Enter how many prime numbers you want: "))
count = 0
num = 2

while count < n:
    # Check if num is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        # num is prime
        print(num, end=" ")
        count += 1
    
    num += 1
