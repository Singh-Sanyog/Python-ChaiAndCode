# class inheritance and isinstance() function
# demostrate the use of insistance to check if my_tesla is an instance of car and ElectricCar.

class Car :
    total_car=0
    def __init__(self,brand ,model):
        self.__brand=brand 
        self.__model=model 
        Car.total_car+=1

class ElectricCar(Car): #inheritace in working
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

my_tesla=ElectricCar("tesla","model s","55kwh")
print(isinstance(my_tesla, ElectricCar)) # for checking instance 
print(isinstance(my_tesla, Car))