#008.	Python Program to check if two Strings are Anagram.

string1=input()
string2=input()
is_anagram=False
for i in range(len(string2)):
    if string1[i]==string2[i]:
       is_anagram=True
    else:
       is_anagram=False
print(f"the given string is {is_anagram}")
