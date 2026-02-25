text=input()
remove_char=input("enter a character you wanted to remove: ")
if remove_char in text:
    text=text.replace(remove_char,"")
    print(text)
else:
    print("character not exist")
print(text)
