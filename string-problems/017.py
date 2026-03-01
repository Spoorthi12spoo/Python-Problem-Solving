#017.Python program to count the Occurrence Of Vowels & Consonants in a String.

String=input().lower()
unique_vowel=""
unique_consonant=""
vowels='aeiou'
for i in String:
    if i in vowels:
        if i not in unique_vowel:
            unique_vowel+=i
    else:
        if i not in unique_consonant:
            unique_consonant+=i
print(f"Unique vowel count: {len(unique_vowel)} unique consonant count: {len(unique_consonant)}")
