class Father:

    def print(self):
        print("Here the Father child called First")

class Mother:

    def print(self):
        print("Here the Mother child called First")

class Child(Father,Mother):

    def __init__(self,name):
        self.name= name

    def print_child(self):
        print("Name of child is :-",self.name)

c = Child("Nilu")
c.print_child()
c.print()