#015. Count word frequency in a sentence using a dictionary.

s="hello world hello"
freq={}
words=s.split()
for word in words:
     if word in freq:
        freq[word]+=1
     else:
        freq[word]=1
print(freq)

#or
freq1={}
words=s.split()
for word in words:
    freq1[word]=freq1.get(word,0)+1
print(freq)
