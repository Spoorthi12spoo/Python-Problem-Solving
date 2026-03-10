#032.Find maximum frequency

max_freq = 0
for ch in count:
    if count[ch] > max_freq:
        max_freq = count[ch]

# Build result string by decreasing frequency
result = ""
for freq in range(max_freq, 0, -1):
    for ch in order:
        if count[ch] == freq:
            result += ch + str(count[ch])

print(result)
