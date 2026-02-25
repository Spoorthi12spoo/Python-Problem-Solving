#003.Write a Python program to count the number of vowels in a given string.

text=input()
vowels='aeiou'
count=0
for i in text:
    if i in vowels:
        count+=1
print(count)
