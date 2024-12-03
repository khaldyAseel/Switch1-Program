# Base class
class Animal:
    def __init__(self, type):
        self.type = type

    def make_sound(self):
        print("hello")

# Derived class for Cat
class Cat(Animal):
    def __init__(self):
        super().__init__("Cat")

    def make_sound(self):
        print("Miao")

# Derived class for Sparrow
class Sparrow(Animal):
    def __init__(self):
        super().__init__("Sparrow")

    def make_sound(self):
        print("tweet tweet")

# Derived class for Dog
class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")

    def make_sound(self):
        print("Woof Woof")

# Function to make sounds
def make_sounds(animals):
    for animal in animals:
        animal.make_sound()

# Usage
cat = Cat()
sparrow = Sparrow()
dog = Dog()
make_sounds([cat, sparrow, dog])
