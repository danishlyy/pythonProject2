file_name = 'programming.txt'

# open 第一个参数：要打开的文件的名称
# open 第二个参数：w 以写入模式打开这个文件
# r 表示读取模式
# a 表示附加模式
# r+ 表示能够读取和写入文件的模式
# 你要写入的文件不存在，函数open()将自动创建它
# 以写入（'w'）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件
# Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式
with open(file_name, 'w') as file_object:
    file_object.write('i love programming.')

# 以下写法，不会换行
with open(file_name, 'w') as file_object:
    file_object.write('i love programming.')
    file_object.write('i think python is easy to deal with text.')

# 以下写法是会换行
with open(file_name, 'w') as file_object:
    file_object.write('i love programming.\n')
    file_object.write('i think python is easy to deal with text.\n')

# 如果只是要给文件添加内容，而不是覆盖原有的内容，可以以附加模式打开文件。
# 以附加模式打开文件时，python不会在返回文件对象前清空文件，而你写入到文件的行都将添加到文件末尾
# 如果指定的文件不存在，python 将为你创建一个空文件
with open(file_name,'a') as file_object:
    file_object.write('i also love finding meaning in large datasets.\n')
    file_object.write('i love creating apps that can run in a browser.\n')
