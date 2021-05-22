# 使用关键字def来告诉Python你要定义一个函数

def greet_user():
    # hello
    print('hello')


greet_user()


def say_hello(name):
    # hello, Zhangsan
    print('hello, ' + name.title())


def display_message(arg):
    # 定义函数的关键字是：def
    print('定义函数的关键字是：' + arg)


def favorite_book(book_name):
    print('one of my favorite book is  %s' % book_name)


# 形参——函数完成其工作所需的一项信息
# 实参是调用函数时传递给函数的信息

say_hello('zhangsan')

display_message('def')

favorite_book('道德经')
