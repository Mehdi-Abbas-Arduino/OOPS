class Car:

    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.__model = model

    def intro(self):
        print("{} {}".format(self.brand,self.__model))
    @property
    def model(self):
        return self.__model
    
my_car = Car("Honda","Civic")
