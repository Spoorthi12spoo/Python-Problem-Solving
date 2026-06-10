#044.Write a program to merge list of dictionaries into one dictionary.
#Example: [{"a":1},{"b":2},{"c":3}] → {"a":1,"b":2,"c":3}

M_D=[{"a":1},{"b":2},{"c":3}]
D={}
for dict in M_D:
    for key in dict:
        D[key]=dict[key]
print(D)
