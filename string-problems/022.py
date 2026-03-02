#022.Python program to remove blank space from string.

text=input()
new_text=''
for i in text:
   
    if i!=' ':
       new_text+=i
print(new_text)

#or 

text=input()
print(text.replace(" ",""))
