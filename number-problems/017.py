#017.Python program to calculate LCM of given two numbers.

import math
a = 12
b = 18

lcm = abs(a * b) // math.gcd(a, b)
print(f"LCM of {a} and {b} is {lcm}")
