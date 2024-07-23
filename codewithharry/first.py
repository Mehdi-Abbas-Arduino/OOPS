# Classes and Objects
class Person:
    name = "Mehdi"
    occupation = "AI Engineer"
    NetWorth = 6000000
    def info(self): # Self is an object for this it is called
        return f"{self.name} is a {self.occupation}"

emp1 = Person()
emp1.name = "Abbas"
emp1.occupation = "Frontend Web Developer"
print(emp1.name)
print(emp1.info())