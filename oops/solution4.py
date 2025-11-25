# encapsulatoion
# modify the car class to encapsulate the brand attribute . making it private, and provide a getter metjod for it.

class Car :
    def __init__(self,brand ,model):
        self.__brand=brand # __ sa name change kardia vriable ka 
        self.model=model 
    
    def get_brand(self):  # get_ -->for getter  - -> is important get name you can change
        return  self.__brand+" !"
    
    def fullname(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car): #inheritace in working
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

my_electric_car=ElectricCar("tesla","ev-s","5500kwh")
print(my_electric_car.battery_size)
print(my_electric_car.fullname())
# print(my_electric_car.__brand)
print(my_electric_car.get_brand())
