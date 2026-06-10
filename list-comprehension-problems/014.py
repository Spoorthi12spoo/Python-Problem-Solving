#014.Create a list of prime numbers less than 20 using list comprehension.

primes = [x for x in range(2, 20) if all(x % i != 0 for i in range(2, x))]
print(primes)
