#012.Python program to replace the string space with a given character.

string = input("enter a string: ")
ch = input("enter a character you wanted to replace: ")

if len(ch) == 1:
    print(string.replace(' ', ch))
else:
    print("enter a single character")

#Python program to replace the string space with a given character using replace() method.

string=input()
ch=input("enter a character: ")
print(string.replace(' ',ch))
