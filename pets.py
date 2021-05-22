# 位置实参：你调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序
# 关键字：使用关键字实参时，务必准确地指定函数定义中的形参名
# 默认值：编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，
# Python将使用指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，
# 可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法
# 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参
# 返回值：函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。函数返回的值被称为返回值。
# 在函数中，可使用return语句将值返回到调用函数的代码行。返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后


def make_pizza_2(size, *toppings):
    """概述要制作的比萨"""
    print('\n making a ' + str(size) + ' pizza with the following toppings:')
    for item in toppings:
        print('- ' + item)


#  making a 16 pizza with the following toppings:
# - pepperoni
make_pizza_2(16, 'pepperoni')
#  making a 12 pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese
make_pizza_2(12, 'mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典,其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
print(user_profile)


def make_pizza_1(*toppings):
    """概述要制作的比萨"""
    print('\n making a pizza with the following toppings:')
    for item in toppings:
        print('- ' + item)


#  making a pizza with the following toppings:
# - pepperoni
make_pizza_1('pepperoni')
#  making a pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese
make_pizza_1('mushrooms', 'green peppers', 'extra cheese')


def describe_pet(pet_name, pet_type="兔子"):
    """显示宠物信息"""
    # I have a 柴犬
    print('I have a %s ' % pet_type)
    # my pet name is 小小柴
    print('my pet name is %s ' % pet_name)


def make_shirt(shirt_size, shirt_logo="i love python"):
    print('shirt size is ' + shirt_size + ' and logo is ' + shirt_logo)


def get_formatted_name(first_name, last_name):
    """返回整洁的名字"""
    full_name = last_name + " " + first_name
    return full_name.title()


def get_formatted_name_middle(first_name, last_name, middle_name=''):
    """返回整洁的名字"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person


def build_person_1(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


def make_album(singer_name, song_name):
    album = {'singe_name': singer_name, 'song_name': song_name}
    return album


name = []
for i in range(0, 3):
    name.append(make_album('刀郎' + str(i), '2002年的第一场雪' + str(i)))

for item in name:
    # {'singe_name': '刀郎0', 'song_name': '2002年的第一场雪0'}
    # {'singe_name': '刀郎1', 'song_name': '2002年的第一场雪1'}
    # {'singe_name': '刀郎2', 'song_name': '2002年的第一场雪2'}
    print(item)


def greet_users(names):
    """向列表中的美味用户都发出简单的问候 接收一个列表"""
    for name in names:
        msg = 'hello,' + name.title() + '!'
        print(msg)


# 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移动至列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # 模拟根据设计制作3D打印模型的过程
    # printing model: dodecahedron
    # printing model: robot pendant
    # printing model: iphone case
    print('printing model: ' + current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型
#  the following moddels have been printed:
# dodecahedron
# robot pendant
# iphone case
print('\n the following moddels have been printed:')
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移至completed_models
    :param unprinted_designs:
    :param completed_models:
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model:' + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print('\n the following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 可以将列表的副本传递给函数，这样函数所做的修改都只影响副本，而丝毫不影响原件
# function_name(list_name[:])
# 切片表示法[:]创建列表的副本
# 传递任意数量的参数
# *toppings 让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


# ('pepperoni',)
make_pizza('pepperoni')
# ('mushrooms', 'green peppers', 'extra cheese')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

user_name_list = ['hanah', 'ty', 'margot']
greet_users(user_name_list)

musician = build_person_1('jimi', 'hendrix', age=27)
# {'first': 'jimi', 'last': 'hendrix', 'age': 27}
print(musician)

musician = build_person('jimi', 'hendrix')
# {'first': 'jimi', 'last': 'hendrix'}
print(musician)

user_name = get_formatted_name_middle('zhang', 'san', 'san')
# Zhang San San
print(user_name)

full_name = get_formatted_name('si', 'li')
# full_name : Li Si
print("full_name : " + full_name)

# 位置实参例子
describe_pet('柴犬', '小小柴')
# 关键字实参例子
describe_pet(pet_type="柯基", pet_name="luck")
# 默认值
describe_pet(pet_name="beauty")
# shirt size is 3 and logo is i wan to sleep
make_shirt('3', 'i wan to sleep')
# shirt size is 1 and logo is i love python
make_shirt(shirt_size='1')
