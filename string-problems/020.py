#020.Python program to count alphabets, digits and special characters.

text=input()
alphabets_count=0
digits_count=0
spcl_char_count=0
for i in text:
    if (i>='A' and i<='Z') or (i>='a' and i<='z'):
        alphabets_count+=1
    elif i>='0' and i<='9':
        digits_count+=1
    else:
        spcl_char_count+=1
print(f"alphabets count: {alphabets_count}\ndigits count:{digits_count}\nspecial characters count {spcl_char_count}")
