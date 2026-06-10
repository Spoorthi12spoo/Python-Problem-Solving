#033.Create a dictionary from a string such that key = character, value = index list.
#Example: "apple" →{'a':[0], 'p':[1,2], 'l':[3], 'e':[4]}

word="apple"   #prefer this
d={}
for i in range(len(word)):
    if word[i] in d:
        d[word[i]]+=[i]
    else:
        d[word[i]]=[i]
print(d)

#or
word="apple"
d={}
index=0
for i in word:
    if i not in d:
        d[i]=[index]
    else:
        d[i]+=[index]
    index+=1
print(d)
