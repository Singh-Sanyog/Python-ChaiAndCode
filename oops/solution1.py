# basic class and object 
# create a car class with attributes like brand and model . then create an instance of this class.

class Car:
    def __init__(self, brand, model): # init ko constructor bhi  kha jata hai 
        self.brand=brand
        self.model=model
        
    # def heelo():
    #     print("hello")
        

my_car= Car("toyta","corolla")
print(my_car.brand)
print(my_car.model)

my_new_car=Car("tata" ,"safari")
print(my_new_car.model)