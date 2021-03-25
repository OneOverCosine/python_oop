# Creating the Reptile class
from animal import Animal

class Reptile(Animal): # passing Animal as an argmument allows Reptile to inherit from it

    def __init__(self):
        super().__init__() # will give Reptile all the attributes declared in __init__ for Animal
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3,4]

    # using a double underscore makes things private
    def __hunt(self):
        return "Bringing home the bacon"

    def use_venom(self):
        return "Stay back! I bite!"

    def seek_warmth(self):
        return "Waiting for that summer weather"