#Encapsulation

class Vehicle:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def __str__(self):
        return f"{self.__brand} {self.__model}"
    
class Schoolbus(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

bus = Schoolbus("Jac Liner", "Jack Line")
    
print(bus)
print("Is the bus and instance of Vehicle?", isinstance(bus, Vehicle))