#014.Python program to convert uppercase char to lowercase of string.

char=input()
print(chr(ord(char)+32))

string=input()
lower_string=' '
for i in string:
    lower_string+=i.lower()
print(lower_string)


ch=input()
print(ch.lower())
