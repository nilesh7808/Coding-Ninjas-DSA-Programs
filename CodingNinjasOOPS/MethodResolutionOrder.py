class Father:
    def __init__(self):
        self.name = "Narendra"
        super().__init__()          # method resolution Order (MRO)

    def print(self):
        print("Here the Father child called First")

class Mother:
    def __init__(self):
        self.name = "Meena"

    def print(self):
        super().__init__()
        print("Here the Mother child called First")

class Child(Mother,Father):

    def __init__(self):
        super().__init__()

    def print(self):
        print("Name of child is :-",self.name)

c = Child()
c.print()
print(Child.mro())