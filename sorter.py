import json

# Load the data from the JSON file
with open('engData.json', 'r') as f:
    data = json.load(f)

# Sort the data based on its values in ascending order
data = sorted(data, key=lambda x: x['id'])

# Write the sorted data to a new JSON file
with open('sorted_data.json', 'w') as f:
    json.dump(data, f, indent=4)
