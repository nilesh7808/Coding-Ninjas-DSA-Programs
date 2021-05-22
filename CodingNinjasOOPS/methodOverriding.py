class vehicle:
    def __init__(self,color):
        self.color = color

    def print(self):
        print("The color of Car is:",self.color)

class Car(vehicle):
    def print_Details(self):
        print("This looks Awesome! ")

    def print(self):
        #self.print()
        print("This is Pretty Good ")
c = Car("Black")
c.print()       # It will find the method of print() in the sub class First if not present then it will look to the parent class(super-class)