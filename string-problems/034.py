#Reverse words in a string using slicing

s = "hello world"
# output → "olleh dlrow"
res=""
start=0
for i in range(len(s)+1):
    if  i==len(s) or s[i]==" " :
        res+=s[start:i][::-1]
        if i!=len(s):
            res+=" "
        start=i+1
print(res)


s1= "hello world"
print(" ".join(word[::-1] for word in s1.split()))

#Remove vowels using slicing and step logic

s = "education"
vowels="aeiou"
res=""
for ch in s:
    if ch not in vowels:
        res+=ch
print(res)

#Remove vowels using slicing and step logic

s = "education"
# remove vowels → "dctn"

#  Left rotate 2 → "cdefab"
s = "abcdef"
print(s[2:]+s[:2])

#Right rotate 2 → "efabcd"
print(s[4:]+s[:4])

#split string into equal parts

s = "abcdefgh"
n=2
parts=[]
for i in range(0,len(s),n):
    parts+=[s[i:i+n]]
print(parts)

# Reverse every alternate word 
s = "one two three four"
words=s.split()
res=""

for i in range(len(words)):
        if i%2==0:
            res+=words[i][::-1]+" "           
        else:
             res+=words[i]+" "
print(res,end=" ")


#Extract only the first and last 3 characters of a string.

string="abcdeeffffxyz"
res=string[:3]+string[-3::]
print(res)

#Expand string: "a3b2c1"
string="a3b2c1"
res=""
for i in range(0,len(string)-1,2):
     char=string[i]
     count=int(string[i+1])
     res+=char*count
print(res)
