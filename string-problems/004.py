#004.Write a Python program to count the number of uppercase and lowercase letters in a string.

text=input()
upper_count=0
lower_count=0
for i in text:
    if i>='A' and i<='Z':
        upper_count+=1
    elif i>='a' and i<='z':
        lower_count+=1
    else:
        print("Invalid input!...enter alphabets only")
        break
    print(f"Uppercase: {upper_count}, lowercase: {lower_count}")
