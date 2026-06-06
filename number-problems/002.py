#002.check armstrong number
   
num=input()
arm=0
for i in num:
    arm+=int(i)**len(num)
if arm==int(num):
    print("armstrong")
else:
    print("not armstrong")


num=int(input())
original_num=num
arm=0
n=len(str(num))
for i in range(len(str(original_num))):
    digit=num%10
    arm+=digit**len(str(original_num))
    num//=10
if arm==original_num:
    print("armstrong")
else:
    print("not armstrong")
