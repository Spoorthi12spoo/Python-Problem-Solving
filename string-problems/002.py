#002.Python Program to count occurrence of a given characters in string.

string=input()
char=input("enter the character to count: ")
count=0
for i in string:
    if i==char:
        count+=1
print(f"{char} appears {count} times")
