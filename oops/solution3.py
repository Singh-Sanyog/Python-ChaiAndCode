#inheritance
#create an ElectricCar class that inherits from the car class and has an additional attribute. battery size

class Car :
    def __init__(self,brand ,model):
        self.brand=brand 
        self.model=model 
    
    def fullname(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car): #inheritace in working
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size


# my_car=Car("tata","neo")
# print(my_car.brand)
# print(my_car.model)
# my_car1=Car("byr","no")
# print(my_car1.brand,my_car.model)
# print(my_car.fullname())
my_electric_car=ElectricCar("tesla","ev-s","5500kwh")
print(my_electric_car.battery_size)
print(my_electric_car.brand)
print(my_electric_car.fullname())