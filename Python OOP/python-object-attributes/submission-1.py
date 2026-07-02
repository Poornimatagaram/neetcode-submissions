class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes
print(f"Initial Attributes : {whiskers.name}, {(whiskers.species)},{whiskers.hunger}, {whiskers.energy}")
# TODO: Modify Whiskers' attributes:
whiskers.hunger = 3
whiskers.energy = 2

# TODO: Print Whiskers' modified attributes
print(f"Initial Attributes : {whiskers.name}, {(whiskers.species)},{whiskers.hunger}, {whiskers.energy}")