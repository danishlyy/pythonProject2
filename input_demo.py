# input的工作原理：函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用
# 使用int()来获取数值输入
# 求模运算符（%）是一个很有用的工具，它将两个数相除并返回余数


if __name__ == '__main__':
    message = input('tell me something and i will repeat it to you')
    print(message)

    name = input('please input your name:')
    print('hello ' + name + '!')
