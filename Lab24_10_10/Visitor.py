# Visitor.py
from Animal import is_show_off

class Visitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"
    
    def visit(self, animal):
        print(f"{self.name} visits {animal.get_name()}")

        if animal.energy < 50:
            print(f"{animal.get_name()} is too tired to interact with {self.name}. Try feeding it")
            # logic for feeding the animal if the visitor wants tp feed
        else:
            print(f"{animal.get_name()} is up and ready to interact")
            is_show_off(animal)
            animal.make_sound()
        print(f"{self.name} leaves {animal.get_name()}")

    def feed(self, animal, food):
        print(f"{self.name} feeds {animal.get_name()} with {food}")
        animal.eat(food)

    def get_name(self):
        return self.name
