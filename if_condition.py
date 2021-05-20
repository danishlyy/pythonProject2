# 每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试
# 在Python中检查是否相等时区分大小写
# 使用and检查多个条件
# 使用or检查多个条件
# 要判断特定的值是否已包含在列表中，可使用关键字in
# 确定特定的值未包含在列表中很重要；在这种情况下，可使用关键字not in

if __name__ == '__main__':
    cars = ['audi', 'bmw', 'subaru', 'toyota']
    for car in cars:
        if car == 'bmw':
            # BMW
            print(car.upper())
        else:
            # Audi
            # Subaru
            # Toyota
            print(car.title())

    # 不等号 !=
    request_topping = 'mushrooms'
    if request_topping != 'anchovies':
        # hold the anchovies
        print('hold the anchovies')

    areas = ['beijing', 'shanghai', 'hangzhou']
    # True
    print('shanxi' not in areas)
    # True
    print('beijing' in areas)

    age = 19
    if age > 18:
        # you are old enough to vote
        print('you are old enough to vote')

    if age > 19:
        print('you can come into bar')
    else:
        # you are so young that you cannot come into the bar
        print('you are so young that you cannot come into the bar')

    if age < 4:
        print('you are free to come into the park')
    elif 4 <= age <= 18:
        print('you have a %s discount' % 8)
    else:
        # you should don not have any discount
        print('you should don not have any discount')

    if age < 4:
        price = 0
    elif age < 18:
        price = 10
    elif age < 65:
        price = 20
    else:
        price = 5
    # you should pay for 20.
    print('you should pay for ' + str(price) + '.')

    names = []
    if names:
        for name in names:
            print(name)
    else:
        # names is empty
        print('names is empty')

    offer_utils = ['a', 'b', 'c']
    customer_request_utils = ['a', 'd', 'e']
    for item in customer_request_utils:
        if item in offer_utils:
            # add:  a
            print('add: ', item)
        else:
            # don not have d
            # don not have e
            print('don not have %s' % item)
    # finish it
    print('finish it')
