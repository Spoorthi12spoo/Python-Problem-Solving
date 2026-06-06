#003.palindrome or not using both iterative and recursive methods

num=int(input())   #for numbers
n=len(str(num))
rev=0
org_num=num
for i in range(n):
    digit=num%10
    rev=digit+rev*10
    num//=10
if org_num==rev:
    print("palindrome")
else:
    print("not palidrome")


rev=''
for i in str:
    rev=i+rev
if str==rev:
    print("palidrome")
else:
    print("not palidrome")



#recursive

def is_palindrome(s,start,end):
    if start>=end:
        return True
    if s[start]!=s[end]:
        return False
    return is_palindrome(s,start+1,end-1)

s=input("enter a string: ").lower().replace(" ","")
if is_palindrome(s,0,len(s)-1):
    print("palindrome")
else:
    print("not palidrome")
