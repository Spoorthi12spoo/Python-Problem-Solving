#025.Python program to remove repeated character from string.

text1="programming"
text2=""
for i in text1:
    if i not in text2:
        text2+=i    
print(text2)
