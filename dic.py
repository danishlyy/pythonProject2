if __name__ == '__main__':
    # 在Python中，字典是一系列键—值对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典
    # 在Python中，字典用放在花括号{}中的一系列键—值对表示
    # 键—值对是两个相关联的值。指定键时，Python将返回与之相关联的值。键和值之间用冒号分隔，而键—值对之间用逗号分隔
    # 要获取与键相关联的值，可依次指定字典名和放在方括号内的键
    # 字典是一种动态结构，可随时在其中添加键—值对。要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值
    # 要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值
    alien_0 = {'color': 'red', 'age': 10}
    # red
    print(alien_0['color'])
    # 10
    print(alien_0['age'])
    # {'color': 'red', 'age': 10}
    print(alien_0)
    alien_0['x_position'] = 40
    alien_0['y_position'] = 50
    # {'color': 'red', 'age': 10, 'x_position': 40, 'y_position': 50}
    print(alien_0)
    alien_0['x_position'] = 50
    # {'color': 'red', 'age': 10, 'x_position': 50, 'y_position': 50}
    print(alien_0)
    # 创建空字典
    dic = {}
    # {}
    print(dic)

    alien_1 = {'x_position': 0, 'y_position': 1, 'speed': 'medium'}
    # original x-position :0
    print('original x-position :' + str(alien_1['x_position']))
    # 向右移动外星人
    # 根据外星人当前速度决定将其移动多远
    if alien_1['speed'] == 'slow':
        x_increment = 1
    elif alien_1['speed'] == 'medium':
        x_increment = 2
    else:
        # 这个外星人的速度一定很快
        x_increment = 3
    # 新位置等于老位置加上增量
    alien_1['x_position'] = alien_1['x_position'] + x_increment
    # new x-position: 2
    print('new x-position: ' + str(alien_1['x_position']))

    # 删除键值对
    alien_2 = {'color': 'yellow', 'points': 4}
    # {'color': 'yellow', 'points': 4}
    print(alien_2)
    del alien_2['points']
    # {'color': 'yellow'}
    print(alien_2)
    # 即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系
    person = {'name': 'peter', 'age': 20, 'gender': 'man'}
    # 字典遍历
    for key, value in person.items():
        # key: name  value: peter
        # key: age  value: 20
        # key: gender  value: man
        print('key:', key, ' value:', value)
    # 遍历key
    for k in person.keys():
        # name
        # age
        # gender
        print(k)
    for k in person:
        # name
        # age
        # gender
        print(k)
    # 要以特定的顺序返回元素，一种办法是在for循环中对返回的键进行排序
    # 可使用函数sorted()来获得按特定顺序排列的键列表的副本
    favorite_languages = {
        'peter': 'java',
        'marry': 'python',
        'jack': 'c++',
        'bob': 'go'
    }
    for name in sorted(favorite_languages.keys()):
        # Bob,thank u for taking the poll
        # Jack,thank u for taking the poll
        # Marry,thank u for taking the poll
        # Peter,thank u for taking the poll
        print(name.title() + ",thank u for taking the poll")

    print('the dic all values:')
    for v in favorite_languages.values():
        # java
        # python
        # c++
        # go
        print(v)

    # 对包含重复元素的列表调用set()，可让Python找出列表中独一无二的元素，并使用这些元素来创建一个集合
    for v in set(favorite_languages.values()):
        # java
        # c++
        # go
        # python
        print(v)

    # 需要将一系列字典存储在列表中，或将列表作为值存储在字典中,这称为嵌套
    # 列表中嵌套字典
    # 字典中嵌套列表
    # 字典中嵌套字典
    alien_a = {'color': 'yellow', 'age': 20}
    alien_b = {'color': 'red', 'age': 21}
    alien_c = {'color': 'green', 'age': 22}
    aliens = [alien_a, alien_b, alien_c]
    for alien in aliens:
        # {'color': 'yellow', 'age': 20}
        # {'color': 'red', 'age': 21}
        # {'color': 'green', 'age': 22}
        print(alien)

    alien_list = []
    for n in range(50):
        alien_single = {'color': 'yellow', 'age': 20}
        alien_list.append(alien_single)

    if alien_list:
        for item in alien_list[:5]:
            # {'color': 'yellow', 'age': 20}
            # {'color': 'yellow', 'age': 20}
            # {'color': 'yellow', 'age': 20}
            # {'color': 'yellow', 'age': 20}
            # {'color': 'yellow', 'age': 20}
            print(item)
    # total numbers of aliens is :50
    print('total numbers of aliens is :' + str(len(alien_list)))

    persons = []
    for n in range(10):
        person_single = {'color': 'green', 'speed': 'slow', 'points': 5}
        persons.append(person_single)

    for n in persons[:3]:
        if n['color'] == 'green':
            n['color'] = 'yellow'
            n['speed'] = 'medium'
            n['points'] = 20

    for p in persons[0:5]:
        # {'color': 'yellow', 'speed': 'medium', 'points': 20}
        # {'color': 'yellow', 'speed': 'medium', 'points': 20}
        # {'color': 'yellow', 'speed': 'medium', 'points': 20}
        # {'color': 'green', 'speed': 'slow', 'points': 5}
        # {'color': 'green', 'speed': 'slow', 'points': 5}
        print(p)

    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese']
    }

    print("you ordered a " + pizza['crust'] + "-crust pizza " + " with the following toppings ")
    for topping in pizza['toppings']:
        # you ordered a thick-crust pizza  with the following toppings
        # 	mushrooms
        # 	extra cheese
        print('\t' + topping)

    users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton'
        },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris'
        }
    }

    for username, user_info in users.items():
        # username : aeinstein
        # username : mcurie
        print('\nusername : ' + username)
        full_name = user_info['first'] + " " + user_info['last']
        location = user_info['location']
        # 	 Full name: Albert Einstein
        # 	 Full name: Marie Curie
        print('\t Full name: ' + full_name.title())
