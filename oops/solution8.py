# property decorators
# use a property decorator in the car class to make the model attribute read-only.

class Car :
    total_car=0
    def __init__(self,brand ,model):
        self.__brand=brand 
        self.__model=model 
        Car.total_car+=1
    
    @property   #decorater
    def model(self):
        return self.__model # now no acces to model to set new value no 
    
    @staticmethod
    def general_description():   
        return "cars are sexy "

mycar=Car("tata","nexon")
# mycar.model="city" -- now it willgive ereor
print(mycar.model)