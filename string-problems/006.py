#006.Count frequency of each character in a string

text = input("Enter a string: ")
char_count = {}
for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

for ch, count in char_count.items():
    print(f"{ch} → {count}")
