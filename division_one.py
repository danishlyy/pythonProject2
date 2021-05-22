print('give me two numbers,and i will divide them.')
print('enter "q" to quit.')
while True:
    first_number = input('\n first number:')
    if first_number == 'q':
        break
    second_number = input('second number:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('you can not divide by 0')
    else:
        print(answer)
