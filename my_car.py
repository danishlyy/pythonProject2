# 导入单个类
from car import Car

my_new_car = Car('奔驰', 'B11', 2021)
print(my_new_car.get_descriptive())
my_new_car.odometer_reading = 40
my_new_car.read_odometer()
