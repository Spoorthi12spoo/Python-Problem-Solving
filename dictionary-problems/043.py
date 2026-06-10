#043.Write a program to convert JSON string into a dictionary.

import json
json_str='{"name": "Alice", "age": 25, "city": "Delhi"}'
dictionary=json.loads(json_str)     #using built in(json.loads() converts json into dict)
print(dictionary)

#or
json_str = '{"name": "Alice", "age": 25, "city": "Delhi"}'

# Remove { } and split into key-value pairs
items = json_str.strip('{}').split(',')

dictionary = {}

for item in items:
    key, value = item.split(':')

    key = key.strip().strip('"')
    value = value.strip().strip('"')

    # Convert numbers
    if value.isdigit():
        value = int(value)

    dictionary[key] = value

print(dictionary)
