#018.Python program to print the highest frequency character in a String.

text=input()
dict={}
for i in text:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
max_char=max(dict,key=dict.get)
print(max_char,dict[max_char])

#without max()
max_char=''
max_count=0 
for ch in dict:
    if dict[ch]>max_count:
        max_count=dict[ch]
        max_char=ch

print(max_char,max_count)

#or
max_freq = max(dict.values())
# Print the characters with maximum frequency
for char in dict:
    if dict[char] == max_freq:
        print(char, end=' ')
