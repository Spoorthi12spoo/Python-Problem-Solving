#018.Python Program to find GCD or HCF of two numbers.

#Method 1: Using Loop (Brute Force)
num1=int(input())
num2=int(input())
smaller=num1 if num1<num2 else num2
for i in range(smaller,0,-1):
    if num1%i==0 and num2%i==0:
        gcd=i
        break
print(gcd)


#Method 2: Using Euclidean Algorithm (Efficient)
a=int(input())
b=int(input())
while(b!=0):   #this logic because, When the remainder becomes 0, it means b perfectly divides a.
    a,b=b,a%b
print(a)

num1=int(input())
num2=int(input())
smaller=num1 if num1<num2 else num2
i=smaller
while(i>0):
    if num1%i==0 and num2%i==0:
        gcd=i
        break
    i=i-1
print(gcd)



#Euclidean recursive
def gcd(num1,num2):
    if num2==0:
       return num1
    else:
        return gcd(num2,num1%num2)
    
num1=int(input())
num2=int(input())

print(gcd(num1,num2))


#brute force recursive
def gcd_bruteforce(a, b, i=None):
    # Use ternary only to find the smaller number
    i = i if i is not None else (a if a < b else b)

   
    if a % i == 0 and b % i == 0:
        return i
    else:
        return gcd_bruteforce(a, b, i-1)

# Example
a = 12
b = 16

print(f"GCD of {a} and {b} is {gcd_bruteforce(a, b)}")
