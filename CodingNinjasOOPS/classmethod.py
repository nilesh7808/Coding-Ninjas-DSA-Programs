from datetime import *
class Student:
    def __init__(self,name,age = 18,percentage = 70 ):
        self.name = name
        self.age = age
        self.percentage = percentage
    @classmethod
    def DateOfBirth(cls,name,year,percentage):
        return cls(name,date.today().year - year,percentage)
    def studentDetails(self):
        print("Name =",self.name)
        print("Age =",self.age)
        print("Percentage =",self.percentage)
s1 = Student("Nilesh")
s1 = Student.DateOfBirth("Nilesh Raj",1999,"80"+"%")
s1.studentDetails()