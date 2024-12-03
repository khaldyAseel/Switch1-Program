class Animal:
    def __init__(self, type):
        self.type = type

class Cat(Animal):
    def __init__(self):
        super().__init__("Cat")

class Sparrow(Animal):
    def __init__(self):
        super().__init__("Sparrow")

def make_sounds(animals):
    for animal in animals:
        sound = ""
        if animal.type == "Cat":
            sound = "Miao"
        elif animal.type == "Sparrow":
            sound = "tweet tweet"
            
        print(sound)

# Usage
cat = Cat()
sparrow = Sparrow()
make_sounds([cat, sparrow])
