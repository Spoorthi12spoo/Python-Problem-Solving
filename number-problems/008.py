#008. Write a program in Python to swap two numbers without using third variable

a=int(input("enter a number: "))
b=int(input("enter a number: "))
a=a+b
b=a-b
a=a-b
print(f"a is {a} b is {b}")
