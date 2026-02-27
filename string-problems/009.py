#009.Python program to check a String is palindrome or not.

string=input().lower()
rev=''
for i in string:
    rev=i+rev
if string==rev:
    print("palindrome")
else:
    print("not palindrome")
