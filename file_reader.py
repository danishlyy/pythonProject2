# 为何会多出这个空行呢？因为read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。
# 要删除末尾的空行，可在print语句中使用 rstrip()
# Python将在当前执行的文件（即.py程序文件）所在的目录中查找文件
# 文件读取：1、相对路径 2、绝对路径
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open('text/chinese.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 以每次一行的方式检查文件，可对文件对象使用for循环
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# 创建一个包含文件各行内容的列表
with open('pi_digits.txt') as file_object:
    # readlines 从文件中读取每一行，并将其存储在一个列表中
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
