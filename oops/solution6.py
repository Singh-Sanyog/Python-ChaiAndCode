# class variables 
# add a class variable to car that keeps track of the number of cars created.

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

Car("tata","nexon")
Car("tata", "safari")
test=Car("test","test")
print(Car.total_car) #do this always
print(test.total_car) # dont do this 

    
    