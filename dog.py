# 在Python中，首字母大写的名称指的是类
# 实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
# 以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量
#

class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


# 创建类的实例
my_dog = Dog('kettle', 6)
your_dog = Dog('Lucy', 12)
# my dog name is Kettle.
print('my dog name is ' + my_dog.name.title() + '.')
# my dog age is 6 years old.
print('my dog age is ' + str(my_dog.age) + ' years old.')
# Kettle is now sitting.
my_dog.sit()
# Kettle rolled over!
my_dog.roll_over()

# your dog name is Lucy.
print('your dog name is ' + your_dog.name.title() + '.')
# your dog age is 12 years old.
print('your dog age is ' + str(your_dog.age) + ' years old.')
# Lucy is now sitting.
your_dog.sit()
# Lucy rolled over!
your_dog.roll_over()


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('restaurant_name:' + self.restaurant_name + "\n" + "cuisine_type: " + self.cuisine_type)

    def open_restaurant(self):
        print('餐馆正在营业中。。。。。')


my_restaurant = Restaurant('天啦小馆', '面食')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
