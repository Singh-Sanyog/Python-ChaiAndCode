# polymorphism  -- > differeent class same method different parameters same class name and method
# demonstrate polymorphism by defining a method fuel_type in both car and electric car classes ,but with different behaviuors.

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
    
    def fuel_type(self):
        return "electric charge"

safari=Car("tata","safari")
Electric=ElectricCar("tsela","no","55kwh")
print(safari.fuel_type())
print(Electric.fuel_type())

