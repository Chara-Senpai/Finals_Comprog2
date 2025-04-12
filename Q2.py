#Inheritance
#Build a class Employee with multiple constructors that 
#can initialize an employee object in different ways.

class Employee:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data: str):
        name, age = data.split (',')
        return cls (name.strip(), int(age.strip()))
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['name'], data['age'])

class Action:
    def movement(self):
        print('The employee is working on:')

class Employee1(Employee, Action):
    def __init__(self, name, age):
        super().__init__(name, age)

    def work1(self):
        print('Calculating sales.')

class Employee2(Employee, Action):
    def work2(self):
        print('Developing.')

class Employee3(Employee, Action):
    def work3(self):
        print('Making an advertisement')

# Creating objects and demonstrating inheritance
employee1 = Employee1.from_string('Bailu, 60')
employee2 = Employee2.from_dict({'name':'Aether','age': 50})
employee3 = Employee3('Rover', 40)

print(f'{employee1.name}, {employee1.age}')
employee1.movement()
employee1.work1()

print(f'{employee2.name}, {employee2.age}')
employee2.movement()
employee2.work2()

print(f'{employee3.name}, {employee3.age}')
employee3.movement()
employee3.work3()
