class Student:
    def __init__(self,name, age=18, percentage = 80):
        # self.name = name    # This is public modifier
        # self.age = age      # This is public modifier
       # self.percentage = percentage    # This is public modifier

        self.__name = name  # This is private modifier
        self.__age = age    # This is private modifier
        self.__percentage = percentage  # This is private modifier

    def studentDetails(self, name, age, percentage):
       # print("Name =", self.name)
       # print("Age =", self.age)                       #These cannot be accessible because all are the private modifiers.
       # print("Percentage =", self.percentage)

        print("Name =",self.__name)
        print("Age =",self.__age)
        print("Percentage =",self.__percentage)

s1 = Student("Nilesh Raj")
#print(s1.name) # This is public modifier of name and we can't access it
#print(s1.__name) # We can't access it so for access it we have to use the Name Mangling
print(s1._Student__name) # Now it is accessible
#print(s1.age)  # This is public modifier of age
s1.studentDetails("Nilesh Raj", 20, 80)