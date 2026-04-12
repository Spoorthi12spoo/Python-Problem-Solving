#018.Check if a list is a palindrome.

l=list(map(int,input().split()))
rev=[]
for i in l:
    rev=[i]+rev
if l==rev:
    print("palindrome")
else:
    print("not palindrome")
