#019.Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.

text=input()
vowel='aeiou'
new_text=''
replaced=False
for i in text:
    if i in vowel and not replaced:
        new_text+='-'
        replaced=True
    else:
        new_text+=i        
print(new_text)

#or

text=input().lower()
vowels='aeiou'
for i in text:
    if i in vowels:
        text=text.replace(i,'-',1)
        break
print(text)
