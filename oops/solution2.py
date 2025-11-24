# class method and self
# add a method to the car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model): # init ko constructor bhi  kha jata hai 
        self.brand=brand
        self.model=model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
        

my_car= Car("toyta","corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car=Car("tata" ,"safari")
print(my_new_car.model)