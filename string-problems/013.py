#013.Python program to convert lowercase char to uppercase of string.

ch=input("enter a character: ")
print(chr(ord(ch)-32))


string=input()
upper_string=''
for i in string:
    upper_string+=i.upper()
print(upper_string)
