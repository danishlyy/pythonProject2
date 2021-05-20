# for循环用于针对集合中的每个元素的一个代码块，而while循环不断地运行，直到指定的条件不满足为止
# 要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break语句。
# break语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执行，从而让程序按你的要求执行你要执行的代码
# 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句

if __name__ == '__main__':
    current_number = 1
    while current_number < 5:
        # 1
        # 2
        # 3
        # 4
        print(current_number)
        current_number += 1

    number = 0
    while number <= 10:
        number += 1
        if number % 2 == 0:
            continue
        print(number)

    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []

    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print('verifying user: ' + current_user.title())
        confirmed_users.append(current_user)
    print('\n the following users have been confirmed:')
    for confirmed_user in confirmed_users:
        print(current_user.title())

    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)
