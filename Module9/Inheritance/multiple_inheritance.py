class Vertebrate:
    def __init__(self, backbone = True):
        self.has_backbone = backbone

    def vertebrate_info(self):
        print("Vertebrates have a backbone")

class Aquatic:
    def __init__(self, habitat="water"):
        self.habitat = habitat

    def aquatic_info(self):
        print("Aquatics live in water")

class Fish (Vertebrate, Aquatic):
    def __init__(self,species, backbone=True, habitat="water"):
        self.backbone = backbone
        self.species = species
        self.habitat = habitat

    def fish_info(self):
        print(f"The {self.species} is a type of fish found in {self.habitat}")

    def swim(self):
        print("The fish is swimming.")

goldfish = Fish("goldfish")
print(goldfish.backbone)
print(goldfish.habitat)
goldfish.aquatic_info()
goldfish.vertebrate_info()
goldfish.fish_info()
goldfish.swim()