# static method are applied on those funcs where they could be access on class but not using instance
class Car:

    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
    def intro(self):
        print("{} {}".format(self.brand,self.model))
    @staticmethod
    def general_description():
        return f"Cars are means of transport."  
print(Car.general_description())