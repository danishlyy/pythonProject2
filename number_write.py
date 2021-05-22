import json

numbers = list(range(0, 10))
filename = 'number.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
