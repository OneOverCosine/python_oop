from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

        self.venom = False # polymorphism for an attribute

    def climb(self):
        return "Hello down there!"

    def constrict(self):
        return "I prefer the term 'hug'..."

    def seek_warmth(self):
        return "I climb trees, I think, to get warm..."

monty = Python()

print(monty.breathe()) # from Animal
print(monty.seek_warmth()) # from Reptile (now from self - polymorphism)
print(monty.use_tongue_to_smell()) # from Snake
print(monty.climb()) # own method