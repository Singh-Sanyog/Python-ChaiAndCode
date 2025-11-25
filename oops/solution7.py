# static method
# add a static method to the Car class taht returns a general descriptive of a car 

class Car :
    total_car=0
    def __init__(self,brand ,model):
        self.__brand=brand # __ sa name change kardia vriable ka 
        self.model=model 
        Car.total_car+=1
    
    def get_brand(self):  # get_ -->for getter  - -> is important get name you can change
        return  self.__brand+" !"
    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or disel"
    
    @staticmethod
    def general_description():  # static method ---> @staticmethod  , as a decoraters its used  
        return "cars are sexy "

mycar=Car("tata","nexon")
#print(mycar.general_description())
#print(mycar.fuel_type())
print(Car.general_description())

