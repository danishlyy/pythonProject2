# 从一个模块中导入多个类
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
# 2019 Volkswagen Beetle
print(my_beetle.get_descriptive())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
# 2016 Tesla Roadster
print(my_tesla.get_descriptive())
