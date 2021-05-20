# 列表由一系列按特定顺序排列的元素组成
# 在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素
if __name__ == '__main__':
    bicycles = ['aaa', 'bbb', 'ccc']
    # ['aaa', 'bbb', 'ccc']
    print(bicycles)
    # 列表是有序集合 要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内
    # bbb
    print(bicycles[1])
    # Aaa
    print(bicycles[0].title())
    # 访问列表的最后一个元素
    # ccc
    print(bicycles[-1])
    message = 'my first bicycle is ' + bicycles[1] + '.'
    print(message)
    names = ['张三', '李四', '王五']
    for x in names:
        # 张三
        # 李四
        # 王五
        print(x)
    for x in names:
        # hello,张三!
        # hello,李四!
        # hello,王五!
        print('hello,' + x + '!')
    # 修改列表的元素
    bicycles[0] = 'bike'
    # ['bike', 'bbb', 'ccc']
    print(bicycles)
    # 列表添加元素
    bicycles.append('subway')
    # ['bike', 'bbb', 'ccc', 'subway']
    print(bicycles)
    # insert()可在列表的任何位置添加新元素
    bicycles.insert(1, 'bus')
    # ['bike', 'bus', 'bbb', 'ccc', 'subway']
    print(bicycles)
    # 创建一个空列表
    names = []
    # []
    print(names)
    # 从列表中删除元素 使用del语句将值从列表中删除后，你就无法再访问它了
    del bicycles[2]
    # ['bike', 'bus', 'ccc', 'subway']
    print(bicycles)
    # 方法pop()可删除列表末尾的元素，并让你能够接着使用它
    pop_result = bicycles.pop()
    # subway
    print(pop_result)
    # ['bike', 'bus', 'ccc']
    print(bicycles)
    # 使用pop()来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可
    # ccc
    print(bicycles.pop(2))
    student_names = ['Jack', 'Peter', 'Mike', 'Jerry']
    # None
    print(student_names.remove('Jack'))
    # 方法remove()只删除第一个指定的值
    scores = [66, 77, 88, 99, 66]
    scores.remove(66)
    # [77, 88, 99, 66]
    print(scores)
    # 使用方法sort()对列表进行永久性排序
    scores.sort()
    # [66, 77, 88, 99]
    print(scores)
    # reverse 逆序
    scores.sort(reverse=True)
    # [99, 88, 77, 66]
    print(scores)
    # 使用函数sorted()对列表进行临时排序
    cars = ['宝马', '奔驰', '奥迪', '雪弗莱']
    # 排序前: ['宝马', '奔驰', '奥迪', '雪弗莱']
    print('排序前:', cars)
    # 排序后: ['奔驰', '奥迪', '宝马', '雪弗莱']
    print('排序后:', sorted(cars))
    # 原始排序: ['宝马', '奔驰', '奥迪', '雪弗莱']
    print('原始排序:', cars)
    # 列表逆序 只是反转列表元素的排列顺序
    cars.reverse()
    # ['雪弗莱', '奥迪', '奔驰', '宝马']
    print(cars)
    # 列表长度
    length = len(cars)
    # cars 列表长度: 4
    print('cars 列表长度:', length)
    for car in cars:
        # car name: 雪弗莱
        # car name: 奥迪
        # car name: 奔驰
        # car name: 宝马
        print('car name:', car)

    for value in range(1, 5):
        # 1
        # 2
        # 3
        # 4
        print(value)
    # 使用range()创建数字列表
    numbers = list(range(1, 6))
    # [1, 2, 3, 4, 5]
    print(numbers)
    # 使用函数range()时，还可指定步长
    even_numbers = list(range(2, 11, 2))
    # [2, 4, 6, 8, 10]
    print(even_numbers)
    # 创建一个列表，其中包含前10个整数（即1～10）的平方
    squares = []
    for value in range(1, 11):
        square = value ** 2
        squares.append(square)
    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(squares)
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 1
    print(min(digits))
    # 10
    print(max(digits))
    # 55
    print(sum(digits))
    # 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
    results = [num ** 2 for num in digits]
    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(results)
    nums = [item for item in range(1, 21)]
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(nums)
    nums_range = [item for item in range(1, 1000001)]
    print(nums_range)
    # 最小值: 1
    print('最小值:', min(nums_range))
    # 最大值 1000000
    print('最大值', max(nums_range))
    # 总和 500000500000
    print('总和', sum(nums_range))
    odd = [i for i in range(1, 21) if i % 2 != 0]
    # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(odd)
    three = [i for i in range(3, 31) if i % 3 == 0]
    # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    print(three)
    cube = [num ** 3 for num in range(1, 11)]
    # 1-10的立方列表: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    print('1-10的立方列表:', cube)
    # 切片
    players = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'qiba']
    # ['zhangsan', 'lisi', 'wangwu']
    print(players[0:3])
    # ['lisi', 'wangwu', 'zhaoliu']
    print(players[1:4])
    # 没有指定第一个索引，Python将自动从列表开头开始
    # ['zhangsan', 'lisi']
    print(players[:2])
    # 从指定位置开始，一直到结尾
    # ['lisi', 'wangwu', 'zhaoliu', 'qiba']
    print(players[1:])
    # ['wangwu', 'zhaoliu', 'qiba']
    print(players[-3:])
    # 遍历切片
    # Zhangsan
    # Lisi
    # Wangwu
    for player in players[:3]:
        print(player.title())
