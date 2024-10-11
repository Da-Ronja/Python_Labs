# Animal.py
from abc import abstractmethod
from unit import herbivore_food, carnivore_food, animal_list
import random

class Animal:
    max_energy = 100
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = self.max_energy # set the initial energy level to the maximum value

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old and has {self.energy} energy"
    
    @abstractmethod
    def eat(self, food):
        pass
    
    def sleep(self):
        print(f"{self.name} sleeps peacefully")
        self.energy = self.max_energy

    @abstractmethod
    def make_sound(self):
        pass

    def use_energy(self, energy_used=10):
        self.energy -= energy_used
        if self.energy <= 0:
            print(f"{self.name} has run out of energy and dies")
            return True
        return False
    
    def get_name(self):
        return self.name
    
    def get_energy(self):
        return self.energy

class Herbivore(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.food = herbivore_food
        self.fear_level = random.randint(1, 10)

    def make_sound(self):
        print(f"{self.name} says: 'I'm a herbivore!")
    
    def run(self):
        if self.energy < 15:
            print(f"{self.name} is too tired to run")
            return True
        else:
            print(f"{self.name} runs away")
            self.energy -= 15
            return False

    def eat(self, food):
        if food in self.food:
            print(f"{self.name} eats {food}")
            self.energy += 5
        else:
            print(f"{self.name} can only eat plantbased food")

class Carnivore(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.food = carnivore_food
        self.agression_level = random.randint(1, 10)

    def make_sound(self):
        print(f"{self.name} says: 'I'm a carnivore!")

    def hunt(self):
        if self.energy <= 25:
            print(f"{self.name} is too tired to continue hunting.")
            return False
        else:
            self.energy -= 25
            return True
    
    def eat(self, food):
        if food in self.food:
            print(f"{self.name} eats {food}")
            self.energy += 10
        else:
            print(f"{self.name} can only eat grass fed animals")


class Lion(Carnivore):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = random.choice(["male", "female"])
        self.color = random.choice(["orange", "blond", "black", "reddish-brown"])

    def make_sound(self):
        print(f"{self.name} says: 'Roar!")
    
    def show_off(self):
        if self.gender == "male":
            print(f"{self.name} shows off its {self.color} mane")
        else:
            print(f"{self.name} dont have a mane instead she stands gracefully")

class Elephant(Herbivore):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.trunk_length = random.randint(1, 10)
        # self.species = "African" # todo: add species to the elephant

    def make_sound(self):
        print(f"{self.name} says: 'Trumpet!")

    def eat(self, food):
        if food in self.food:
            print(f"{self.name} eats {food}")
            self.energy += 15
        else:
            print("Elephants can only eat plants and fruits")

    def trumpet(self):
        print(f"{self.name} trumpets has a trunk length of {self.trunk_length}")

class Giraffe(Herbivore):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.neck_length = random.randint(1, 10)
        self.color = random.choice(["orange", "blond", "black", "reddish-brown"])
        self.food = ["leaves"]

    def make_sound(self):
        print(f"{self.name} says: 'Grunt!")

    def eat(self, food):
        if food in self.food:
            print(f"{self.name} eats {food}")
            self.energy += 10
        else:
            print("Giraffes can only eat leaves")

    def show_off(self):
        print(f"{self.name} shows off its {self.color} spots and has a neck length of {self.neck_length}")

def is_show_off(animal):
    if isinstance(animal, Lion):
        animal.show_off()
    elif isinstance(animal, Elephant):
        animal.trumpet()
    elif isinstance(animal, Giraffe):
        animal.show_off()
    else:
        print(f"{animal.name} does not show off")


### Methods for animals

def init_animals():
    animals = []
    animal_classes = [Lion, Elephant, Giraffe]

    for i, animal in enumerate(animal_list):
        name, age = animal
        animal_class = animal_classes[i % len(animal_classes)]
        animals.append(animal_class(name, age))

    return sort_animals(animals)

def sort_animals(animals):
    the_lions = []
    the_elephants = []
    the_giraffes = []

    for animal in animals:
        if isinstance(animal, Lion):
            the_lions.append(animal)
        elif isinstance(animal, Elephant):
            the_elephants.append(animal)
        elif isinstance(animal, Giraffe):
            the_giraffes.append(animal)
        
    return the_lions, the_elephants, the_giraffes

def remove_dead_animals(animals):
    for animal in animals:
        if animal.use_energy():
            animals.remove(animal)
            print(f"{animal.name} has died")
    return animals

def show_animals(animals):
    for animal in animals:
        print(animal)

def low_energy(animal):
    if animal.energy <= 25:
        print(f"{animal.get_name()} is sleeping. Come back later")
        animal.sleep()
        return True
    return False

def go_hunting(killer, prey):
    if isinstance(killer, Carnivore) and isinstance(prey, Herbivore):
        if killer.agression_level > prey.fear_level:
            print(f"{killer.name} is hunting {prey.name}")
            while killer.energy > 0 and prey.energy > 0:
                print(f"{prey.name} is running away with {prey.energy} energy and {prey.fear_level} fear level!")
                print(f"{killer.name} is running away with {killer.energy} energy")
                is_runing = prey.run() 
                is_hunting = killer.hunt()

                if is_runing:
                    print(f"{prey.name} has been caught by {killer.name}")
                    prey.energy = 0
                    break
                elif not is_hunting:
                    print(f"{killer.name} is too tired to hunt his energy is {killer.energy}")
                    break
                else:
                    print(f"{killer.name} is hunting {prey.name}")
        if killer.agression_level < prey.fear_level:
            print(f"{prey.name} is running away from {killer.name}")
            prey.run()
            killer.energy -= 5
        if killer.agression_level == prey.fear_level:
            print(f"{killer.name} and {prey.name} are playing together")

    elif isinstance(killer, Herbivore) and isinstance(prey, Carnivore):
        print(f"{killer.name} gets afraid and is running away from {prey.name}")
        killer.run()
    else:
        print(f"{killer.name} gets ready to attack {prey.name}")
        go_playing(killer, prey)


def go_playing(animal1, animal2):
    if isinstance(animal1, Carnivore) and isinstance(animal2, Herbivore) and not animal1.agression_level == animal2.fear_level:
        if animal1.agression_level > animal2.fear_level:
            print(f"{animal1.name} is hunting {animal2.name}")
        else:
            print(f"{animal1.name} leaves {animal2.name} alone")
        go_hunting(animal1, animal2)
    elif isinstance(animal1, Herbivore) and isinstance(animal2, Carnivore) and not animal1.fear_level == animal2.agression_level:
        print(f"{animal1.name} is running away from {animal2.name}")
        animal1.run()
    else:
        print(f"{animal1.name} and {animal2.name} are playing together")

def animal_interaction(two_animals):
    playing_or_hunting = random.choice([True, False])

    if playing_or_hunting:
        go_playing(two_animals[0], two_animals[1])
    else:
        go_hunting(two_animals[0], two_animals[1])

