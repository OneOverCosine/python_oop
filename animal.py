# creating the first class
class Animal():
    
    # name = "Cat" # class variable, or attribute
    def __init__(self): # self refers to the current class
        self.alive = True
        self.spine = True
        self.lungs = True

    def move(self):
        return "Moving..."

    def eat(self):
        return "Eating."

    def breathe(self):
        return "Breathing..."
