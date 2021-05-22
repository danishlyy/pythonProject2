file_name = 'question_answer.txt'

with open(file_name, 'w') as file_object:
    question = 'why you like programming?'
    while True:
        user_name = input('please enter your name:\n')
        if user_name == 'quit':
            break
        user_answer = input('your reason:\n')
        message = user_name + " : " + user_answer + '\n'
        print(message)
        file_object.write(message)


