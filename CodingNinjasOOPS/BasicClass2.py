class Student:
    pass
s1 = Student()
s2 = Student()
s3 = Student()
s1.name = "Nilesh Raj"
s2.RollNumber = 1
s3.name = "Ashish"
s3.RollNumber = 2
print(s1.name)
print(s2.RollNumber)
print(s3.name,s3.RollNumber)
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
print(hasattr(s1,"name"))
print(getattr(s1,"name"))
print(hasattr(s2,"name"))
print(getattr(s2,"RollNumber"))
print(hasattr(s2,"RollNumber"))
print(hasattr(s3,"RollNumber"))
print(getattr(s3,"name"))
print(hasattr(s3,"name"))
print(getattr(s3,"RollNumber"))
