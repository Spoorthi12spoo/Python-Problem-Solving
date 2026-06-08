#029.Filter dictionary to keep only keys starting with a vowel.
#Example:{"apple": 2, "bat": 3, "orange": 5} → {"apple":2, "orange":5}

D={"apple": 2, "bat": 3, "orange": 5}
vowel_D={}
for key,value in D.items():
    if key[0].lower() in 'aeiou':
        vowel_D[key]=value
print(vowel_D)
