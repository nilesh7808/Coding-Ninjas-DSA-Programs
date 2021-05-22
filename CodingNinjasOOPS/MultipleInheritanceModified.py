class Father:
    def __init__(self):
        self.name = "Narendra"

    def print(self):
        print("Here the Father child called First")

class Mother:
    def __init__(self):
        self.name = "Meena"

    def print(self):
        print("Here the Mother child called First")

class Child(Mother,Father):

    def __init__(self):
        super().__init__()

    def print_child(self):
        print("Name of child is :-",self.name)

c = Child()
c.print_child()
c.print()