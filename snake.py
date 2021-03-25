# creating a Snake class
from reptile import Reptile

class Snake(Reptile):
    
    def __init__(self):
        super().__init__()
        self.limbs = False
        self.venom = True
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "Blep"

    def shed_skin(self):
        return "I'm blue"

snek = Snake()

# print(snek.eat()) # inherited from the Animal class
# # print(snek.hunt()) # from the Reptile class # hunt() had now been made private
# print(snek.use_tongue_to_smell()) # from Snake
# # Multiple inheritance
