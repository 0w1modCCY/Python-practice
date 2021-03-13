class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1;
        print("So far", self.x)

a = PartyAnimal("Victor")
a.party()
