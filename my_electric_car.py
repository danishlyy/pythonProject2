from car import ElectricCar

my_electric_car = ElectricCar('ele', 'model s', 1990)
# 1990 Ele Model S
# this car has a 70 -kwh battery.
# this car can go approximately 240 miles on a full charge
print(my_electric_car.get_descriptive())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
