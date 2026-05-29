#007.	Convert a tuple into a list.

my_list=(8,9,20,11,20)
print(tuple(my_list))

#or
my_tuple=()
for item in my_list:
    my_tuple+=(item,)
print(my_tuple)
