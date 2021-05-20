if __name__ == '__main__':
    # 列表复制
    my_foods = ['apple', 'pear', 'orange']
    # my favorite foods are: ['apple', 'pear', 'orange']
    print('my favorite foods are:', my_foods)
    friend_foods = my_foods[:]
    # my friend's favorite foods are: ['apple', 'pear', 'orange']
    print('my friend\'s favorite foods are:', friend_foods)
    my_foods.append('pizza')
    # my foods: ['apple', 'pear', 'orange', 'pizza']
    print('my foods:', my_foods)
    friend_foods.append('ice cream')
    # my friend foods: ['apple', 'pear', 'orange', 'ice cream']
    print('my friend foods:', friend_foods)
    # Python将不能修改的值称为不可变的，而不可变的列表被称为元组
    # 元组定义：使用圆括号进行定义
    # 元组访问：使用索引下标来访问元组中的元素
    # 元组使用场景：如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组
    dimensions = (200, 50)
    # 200
    print(dimensions[0])
    # 50
    print(dimensions[1])
    # 元组遍历
    print('origin dimensions:')
    for item in dimensions:
        # origin dimensions:
        # 200
        # 50
        print(item)
    dimensions = (20, 40)
    print('modified dimensions')
    for item in dimensions:
        # modified dimensions
        # 20
        # 40
        print(item)
