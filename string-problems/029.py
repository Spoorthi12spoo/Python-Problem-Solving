#029.Python Program to sort characters of string in ascending order.

string1 = input()
sorted_str = ""

while string1:  # Repeat until string1 is empty
    ascending = string1[0]  # Assume first char is smallest
    for ch in string1:
        if ch < ascending:
            ascending = ch
    sorted_str += ascending
    string1 = string1.replace(ascending, "", 1)  # Remove first occurrence
print(sorted_str)


#we can also use bubble sort which is more efficient
string1 = input("Enter a string: ")

# Convert string to list to allow swapping
char_list = list(string1)

# Bubble sort
n = len(char_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if char_list[j] > char_list[j + 1]:
            # Swap if previous char is greater than next char
            char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]

# Convert list back to string
sorted_string = ''.join(char_list)
print("String in ascending order:", sorted_string)
