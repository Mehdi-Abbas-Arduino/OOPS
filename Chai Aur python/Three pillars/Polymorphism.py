class Car:

    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model

    def intro(self):
        print("{} {}".format(self.brand,self.model))

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model,batterysize):
        super().__init__(brand, model)
        # Car.__init__(brand,model)
        self.batterysize = batterysize
    def fuel_type(self):
        return "Electric Charge"

My_tesla = ElectricCar("Tesla","CyberTruck","90Kwh")

print(My_tesla.batterysize)
My_tesla.intro()
print(My_tesla.fuel_type())

Safari = Car("TATA","Safari")
print(Safari.fuel_type())