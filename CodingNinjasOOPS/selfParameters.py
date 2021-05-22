class Student:
    passingPercentage = 40
    def details(self):
        self.name = "Nilesh Raj"
        self.percentage = 80
        # print("My Name is",self.name)

    def isPassed(self):
        if self.percentage > Student.passingPercentage:
            print("Student is passed")
            # print(self.percentage)
            # print(self.name)
            # print(self.passingPercentage)
        else:
            print("Student is not paased")
        pass
s1 = Student()
s1.details()
s1.isPassed()