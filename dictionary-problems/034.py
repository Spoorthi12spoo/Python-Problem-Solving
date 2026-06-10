#034.Check if two dictionaries are equal (same keys & values)
D1={'a': [0], 'p': [1, 2], 'l': [3], 'e': [4]}
D2={'a': [0], 'p': [1, 2], 'l': [3], 'e': [4]}
if D1==D2:
    print("two dictionaries are equal")
else:
    print("not equal")

#without ==

D1={'a': [0], 'p': [1, 2], 'l': [3], 'e': [4]}
D2={'a': [0], 'p': [1, 2], 'l': [3], 'e': [4]}
if len(D1)!=len(D2):
    print("not equal")
else:
    equal=True
    for key in D1:
        if key not in D2 or D1[key]!=D2[key]:
            equal=False
            break
    if(equal):
        print("two dictionaries are equal")
    else:
        print("not equal")
