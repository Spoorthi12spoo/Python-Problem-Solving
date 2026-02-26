#007.Count digits and alphabets separately in a string.

text=input()
alpha_count=0
digit_count=0
for i in text:
    if (i>='A' and i<='Z') or (i>='a' and i<='z'):
        alpha_count+=1
    elif i>='0' and i<='9':
        digit_count+=1
    else:
       continue
print(f"alphabets count: {alpha_count},digit count: {digit_count}")
