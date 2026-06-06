#001.reverse an integer

num=input()
rev=" " 
for i in num:
    rev=i+rev
print(int(rev))

#Mathematical version (using while)
num = int(input("Enter an integer: "))
reversed_num = 0

while num != 0:   
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed integer:", reversed_num)

#using for loop
num=int(input("enter a number:"))
rev=0
for i in range(len(str(num))):
    digit=num%10
    rev=rev*10+digit
    num//=10
print(rev)

#using while
num=input()
rev=''
i=len(num)-1
while(i>=0):
    rev=rev+num[i]
    i=i-1
print(int(rev))
