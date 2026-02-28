#015.Python program to convert lowercase vowel to uppercase in string.   

string=input("enter a string: ")
vowel='aeiou'

for i in string:
    if i in vowel:
        upper_char=i.upper()
        string=string.replace(i,upper_char)

print(string)
