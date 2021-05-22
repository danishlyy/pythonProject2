# 修改属性的值：1、直接通过实例进行修改 2、通过方法进行设置 3、通过方法进行递增（增加特定的值）
# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，而新类称为子类。
# 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
# 创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值。为此，子类的方法__init__()需要父类施以援手
# 创建子类时，父类必须包含在当前文件中，且位于子类前面
# 定义子类时，必须在括号内指定父类的名称
# super()是一个特殊函数，帮助python吧父类和子类关联起来


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('this car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cannot roll back an odometer')

    def increment_odometer(self, mileage):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        """汽车没有油箱"""
        print('this car need a'
              ' gas tank')


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('this car has a ' + str(self.battery_size) + ' -kwh battery.')

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = 'this car can go approximately ' + str(range)
        message += ' miles on a full charge'
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.battery_size = 70
        # 将类作为一个实例属性
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('this car has a ' + str(self.battery_size) + ' -kwh battery')

    # 子类重写父类的方法
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print('this car does not need a gas tank')

# my_tesla = ElectricCar('tesla', 'model s', 2020)
# print(my_tesla.get_descriptive())
# my_tesla.battery.battery_size
# my_tesla.fill_gas_tank()
# my_tesla.battery.get_range()
# my_new_car = Car('audi', 'a4', 2018)
# print(my_new_car.get_descriptive())
# # 直接修改属性值
# my_new_car.odometer_reading = 23
# # 通过方法进行修改属性值
# my_new_car.update_odometer(44)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(20)
# my_new_car.read_odometer()
