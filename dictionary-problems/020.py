#020.Create a dictionary that groups words by their first letter.*

#Example:
#["apple","ant","banana"] → {'a': ["apple","ant"], 'b': ["banana"]}

l=["apple","ant","banana"]
D={}
for word in l:
    if word[0] in D:
          D[word[0]]+=[word]
    else:
          D[word[0]]=[word]
print(D)

