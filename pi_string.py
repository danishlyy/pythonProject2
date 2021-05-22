# 读取文本文件时，Python将其中的所有文本都解读为字符串。
# 如果你读取的是数字，并要将其作为数值使用，就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# 3.142592653589793238462643383279
print(pi_string)
# 36
print(len(pi_string))

file_name_1 = 'pi_million_digits.txt'

with open(file_name_1) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('enter your birthday,in the form mmddyy:')

if birthday in pi_string:
    print('your birthday appears in the first million digits of pi!')
else:
    print('your birthday does not appear in the first million digits of pi.')

print(pi_string[:52] + "...")
print(len(pi_string))
