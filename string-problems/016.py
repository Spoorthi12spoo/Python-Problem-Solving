#016.python program to delete vowels in a given string.

string=input()
vowels='aeiou'
res=''
for i in string:
    if i in vowels:
        i=''
    res+=i
print(res)
