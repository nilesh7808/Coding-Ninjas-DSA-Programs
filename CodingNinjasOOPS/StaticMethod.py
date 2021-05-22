class Student:
    xyx = "Hello"
    def Names(self):
        self.name = "Nilu"
    def Roll_No(self):
        self.RollNo = 1
        print("Roll No.",self.RollNo,self.name)
    @staticmethod
    def WelcomeToSchool():
        print("Hey! There, Welcome to the School ")

s1 = Student()
s1.Names()
s1.Roll_No()
s1.WelcomeToSchool()