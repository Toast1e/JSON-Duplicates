import json

with open('example.json') as f:
    data = json.load(f)

unique_values = {}
for item in data:
    for value in item.values():
        if value in unique_values:
            unique_values[value] += 1
        else:
            unique_values[value] = 1

duplicates = [value for value, count in unique_values.items() if count > 1]
print(duplicates)
