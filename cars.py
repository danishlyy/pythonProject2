# 导入整个模块
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
# 2019 Volkswagen Beetle
print(my_beetle.get_descriptive())
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
# 2016 Tesla Roadster
print(my_tesla.get_descriptive())