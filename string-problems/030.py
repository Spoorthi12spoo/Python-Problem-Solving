#030.Count only vowels

text="education"
vowel_count={}
for i in text:
    if i in 'aeiou':
        if i in vowel_count:
            vowel_count[i]+=1
        else:
            vowel_count[i]=1
for key,value in vowel_count.items():
    print(key,str(value),sep="",end="")

#or
text = "education"
vowel_count = {}

for ch in text:
    if ch in "aeiou":
        vowel_count[ch] = vowel_count.get(ch, 0) + 1
result = ''.join(str(k) + str(v) for k, v in vowel_count.items())
print(result) 
