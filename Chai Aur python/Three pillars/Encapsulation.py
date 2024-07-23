# In encapsulation we make a private variable which could be access only by making getter methods 


class Car:

    def __init__(self,brand,model) -> None:
        self.__brand= brand
        self.model = model

    def intro(self):
        print("{} {}".format(self.__brand,self.model))
    
    def get_brand(self):
        return self.__brand
class ElectricCar(Car):
    def __init__(self,brand, model,batterysize):
        super().__init__(brand, model)
        # Car.__init__(brand,model)
        self.batterysize = batterysize

My_tesla = ElectricCar("Tesla","CyberTruck","90Kwh")

print(My_tesla.batterysize)
My_tesla.get_brand()
My_tesla.intro()
