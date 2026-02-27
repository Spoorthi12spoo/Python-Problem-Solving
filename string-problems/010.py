#10.Python program to check given character is vowel or consonant.

ch=input("enter a character: ").lower()
vowels='aeiou'
if len(ch)==1 and ch.isalpha():
    if ch in vowels:
        #without in:  if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print("vowel")
    else:
        print("consonant") 
else:
    print("enter single alphabet only.") 
