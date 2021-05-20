if __name__ == '__main__':
    name = 'ada love'
    # Ada Love
    print(name.title())
    # ada love
    print(name.lower())
    # ADA LOVE
    print(name.upper())
    first_name = 'san'
    last_name = 'zhang'
    full_name = last_name + ' ' + first_name
    # zhang san
    print(full_name)
    # hello,zhang san!
    print('hello,' + full_name + '!')
    message = 'hello,' + full_name + '!'
    print(message)
    # python
    print('python')
    # 	python
    print('\tpython')
    # language:
    #  python
    #  vue
    #  java
    print('language:\n python \n vue \n java')
    # language:
    # 	 python
    # 	 vue
    # 	 java
    print('language:\n\t python \n\t vue \n\t java')
    # 去除空白
    language_left = ' python'
    # python lstrip() 去除左边空格
    print(language_left.lstrip())
    language_right = 'python '
    # python rstrip() 去除右边空格
    print(language_right.rstrip())
    language_all = ' python '
    # python strip() 去除两边空格
    print(language_all.strip())
    # str() 将值转换为字符串
    age = 23
    print('hello,' +  str(age) + 'rd,birthday')
    # 8
    print(5 + 3)
    # 8.0
    print(16 / 2)
    # 8
    print(2 * 4)
    # 8
    print(10 - 2)