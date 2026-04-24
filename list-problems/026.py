#026.Sort a list of strings by length and alphabetical order

l=["apple", "bat", "banana", "cat", "dog"]
for i in range(len(l)):
    for j in range(i+1,len(l)):
            # Compare by length first
        if len(l[j]) < len(l[i]):
            l[i], l[j] = l[j], l[i]
        # If lengths are same, compare alphabetically
        elif len(l[j]) == len(l[i]) and l[j] < l[i]:
            l[i], l[j] = l[j], l[i]
print(l)
