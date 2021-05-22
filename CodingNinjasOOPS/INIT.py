# class Student:
#     def __init__(self):
#         self.name = "Nilesh"
#         self.RollNumber = 1
#         print(self.RollNumber, self.name)
#
#
# s1 = Student()
# print(s1.__dict__)
# s2 = Student()
# s2.name = "Neeraj"
# s2.RollNumber = 2
# print(s2.__dict__)
# s3 = Student()
# s3.name = "Ashish"
# s3.RollNumber = 3
# print(s3.__dict__)
class Student:
    def __init__(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber
s1 = Student("Nilesh", 1)
print(s1.__dict__)
print(s1.name,s1.rollNumber)
s2 = Student("Ashish", 2)
print(s2.__dict__)
print(s2.name,s2.rollNumber)
s3 = Student("Niraj", 3)
print(s3.__dict__)
print(s3.name,s3.rollNumber)