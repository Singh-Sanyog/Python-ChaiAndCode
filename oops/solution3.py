#inheritance
#create an ElectricCar class that inherits from the car class and has an additional attribute.

class Car :
    def __init__(self,brand ,model):
        self.brand=brand 
        self.model=model 


my_car=Car("tata","neo")
print(my_car.brand)
print(my_car.model)
my_car1=Car("byr","no")
print(my_car1.brand,my_car.model)