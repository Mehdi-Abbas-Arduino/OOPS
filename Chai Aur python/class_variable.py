class Car:

    No_of_Cars = 0
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
        Car.No_of_Cars += 1
    def intro(self):
        print("{} {}".format(self.brand,self.model))


my_tesla = Car("Tesla","Model S")

civic = Car("Honda","Civic")

print(Car.No_of_Cars)