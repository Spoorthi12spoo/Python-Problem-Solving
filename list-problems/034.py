#034.Print only even or odd numbers from a nested list.

def print_even(l):
    for i in l:
        if isinstance(i, list):
            print_even(i)     # if i is a list → go deeper
        else:
            if i % 2 != 0:    # if i is even
                print(i)

l = [1, [2, [3, 4], 5], [6, 7, [8, 9]]]
print("Even numbers:")
print_even(l)
