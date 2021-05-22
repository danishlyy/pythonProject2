file_name = 'guest.txt'

with open(file_name, 'w') as file_object:
    name = input('please enter your name:')
    file_object.write(name)
