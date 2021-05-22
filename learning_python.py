file_name = 'learn_python.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

result = ''

for line in lines:
    result += line.strip().replace('python', 'JavaScript')

print(result)
