#Polymorphism and Duck Typing 

class SchoolOne:
    def __init__(self):
        self.name = "SchoolOne"
        self.students = {
            "John": [90, 95, 99],
            "George": [70, 100, 85]
        }

    def display_info(self):
       print(f"\n{self.name}")
       for student, grades in self.students.items():
           avg = sum(grades) / len(grades)
           gpa = self.calculator(grades)
           print(f"{student} Average = {avg:2f}, GPA = {gpa:.2f}")

    def calculator(self, grades):
        return sum(self.overall_gpa(g) for g in grades) / len(grades)
    
    def overall_gpa(self, grades):

        if grades >= 90:
            return 4.0
        
        elif grades >= 80:
            return 3.0
        
        elif grades >= 70:
            return 2.0
        
        elif grades >= 60:
            return 1.0
        
        else:
            return 0.0

class SchoolTwo:
    def __init__(self):
        self.name = "SchoolTwo"
        self.students = {
            "Nihon": [80, 70, 90],
            "Barbok": [99, 70, 60]
        }

    def display_info(self):
       print(f"\n{self.name}")
       for student, grades in self.students.items():
           avg = sum(grades) / len(grades)
           gpa = self.calculator(grades)
           print(f"{student} Average = {avg:2f}, GPA = {gpa:.2f}")

    def calculator(self, grades):
        return sum(self.overall_gpa(g) for g in grades) / len(grades)
    
    def overall_gpa(self, grades):

        if grades >= 90:
            return 4.0
        
        elif grades >= 80:
            return 3.0
        
        elif grades >= 70:
            return 2.0
        
        elif grades >= 60:
            return 1.0
        
        else:
            return 0.0


def school_data(school):
    school.display_info()

schoolone = SchoolOne()
schooltwo = SchoolTwo()

school_data(schoolone)
school_data(schooltwo)