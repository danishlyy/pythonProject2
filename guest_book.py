file_name = 'guest_book.txt'

with open(file_name, 'w') as file_object:
    while True:
        name = input('please your name:')
        if name == 'quit':
            break
        message = 'hello,' + name + '\n'
        print(message)
        file_object.write(message)
