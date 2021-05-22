file_name = 'alice.txt'

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'sorry,the file ' + file_name + ' does not exist.'
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    number_of_words = len(words)
    print('the file ' + file_name + ' has about ' + str(number_of_words) + ' words.')
