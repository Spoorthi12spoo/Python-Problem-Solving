#028.Python program to copy one string to another string.

string1=input()
string2=''     #or string2=string1[:]
for i in string1:
    string2+=i
print(string2)
