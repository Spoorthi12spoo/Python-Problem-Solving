#STRING SLICING

#Extract a substring from a string

s = "abcdef"   #get "bcd"
print(s[1:4])

#Extract first n characters

s = "hello"
# get "hel" (first 3 chars)
print(s[0:3])

#Extract last n characters

s = "hello"
# get "llo"
print(s[2:])

#Extract a substring from index i to end

s = "python"
# get "thon" (from index 2)
print(s[2:])

#Extract a substring with step

s = "abcdef"
# get "ace" (every second character)
print(s[::2])

#Reverse a string using slicing

s = "python"
# get "nohtyp"
print(s[::-1])

#2. Intermediate Patterns

#Print every n-th character

s = "abcdefgh"
# every 3rd char → "adg"
print(s[::3])

#Remove first and last characters

s = "python"
# result → "ytho"

print(s[1:5])

#Remove every n-th character

s = "abcdef"
# remove every 2nd → "ace"
print(s[1::2])

#Print alternate characters

s = "abcdef"
# output → "ace"
print(s[::2])

