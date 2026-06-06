#019.Python Program to Convert Decimal Number into Binary.

num = int(input("Enter a decimal number: "))
binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
print("Binary:", binary)


num=int(input())
binary=''
if num==0:
    binary=0
else:
  for i in range(num.bit_length()):  #bit_length() → gives how many bits are needed to represent the number in binary.
#Example: 10.bit_length() = 4 → binary uses 4 bits (1010).
        binary=str(num%2)+binary
        num//=2
print(binary)
