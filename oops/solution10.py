# multiple inheritance 
# create two classes battery and engine , and let the ElectricCar class inherit from both , demostrating multiple inheritance.

class Car :
    total_car=0
    def __init__(self,brand ,model):
        self.__brand=brand 
        self.__model=model 
        Car.total_car+=1

class Battery:
    def battery_info(self):
        return "55 kwh"

class Engine:
    def engine_info(self):
        return "harley"


class ElectricCar(Car,Battery,Engine): #inheritace in working
    pass

my_tesla=ElectricCar("tesla","model S")
print(my_tesla.battery_info())
print(my_tesla.engine_info())