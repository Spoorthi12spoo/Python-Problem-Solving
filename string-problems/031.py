#031.Print characters in order of frequency
#Input: "aabbccc" → Output: "c3a2b2"

text = "aabbccc"
count = {}
order = []

# Count characters and store first appearance order
for ch in text:
    if ch not in count:
        count[ch] = 1
        order.append(ch)  # remember first appearance
    else:
        count[ch] += 1
