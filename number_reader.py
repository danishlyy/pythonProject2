import json

filename = 'number.json'

with open(filename)  as file_object:
    numbers = json.load(file_object)
print(numbers)