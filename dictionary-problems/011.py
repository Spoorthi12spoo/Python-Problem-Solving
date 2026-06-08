#011.Convert a nested dictionary into a flattened dictionary.
#Example: Input → {'a': {'b': 1}}  Output → {'a_b': 1}

D={'a': {'b': 1}}
flat={}
for key,value in D.items():
    for inner_key,inner_value in value.items():
        flat[key+ '_'+inner_key]=inner_value
print(flat)

#if we want to perform this in same dictionary we have to convert into list,
# otherwise python will raise RuntimeError: dictionary changed size during iteration
#While looping over D.items(), you added a new key (key + '_' + inner_key).

#Python doesn’t allow adding/removing keys from a dictionary during iteration.

D={'a': {'b': 1}}

for key,value in list(D.items()):
    for inner_key,inner_value in value.items():
        D[key + '_'+inner_key]=inner_value
    del D[key]
print(D)
