#Abstraction

from abc import ABC, abstractmethod

class MainVector(ABC):

    @abstractmethod
    def add(self, other):
        pass

class Vector(MainVector):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __add__(self, other):
        return self.add(other)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(5, 10)
v2 = Vector(6, 9)
v3 = v1 + v2

print(v3)
        

