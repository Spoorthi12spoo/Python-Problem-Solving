#014.Find the maximum and minimum values in a numeric tuple.

t=(1,2,3,4,5,6)
maximum=t[0]
for i in t:
    if i>maximum:
        maximum=i
print(maximum)
print(max(t))
   
minimum=t[0]
for i in t:
    if i< minimum:
        minimum=i
print(minimum)
print(min(t))


#max and min together

t = (10, 25, 5, 40, 15)
max_val = t[0]
min_val = t[0]

for i in t:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum:", max_val)
print("Minimum:", min_val)
