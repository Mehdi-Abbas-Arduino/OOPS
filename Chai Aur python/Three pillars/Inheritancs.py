class Car:

    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model

    def intro(self):
        print("{} {}".format(self.brand,self.model))

class ElectricCar(Car):
    def __init__(self, brand, model,batterysize):
        super().__init__(brand, model)
        # Car.__init__(brand,model)
        self.batterysize = batterysize

My_tesla = ElectricCar("Tesla","CyberTruck","90Kwh")

print(My_tesla.batterysize)
My_tesla.intro()