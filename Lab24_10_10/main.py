# main.py
from Animal import init_animals, animal_interaction
from zoo_helpers import visit_animal
from Visitor import Visitor
from unit import at_the_zoo, animal_food
import random

def show_menu(at_the_zoo):
    choise = 0

    print("What would you like to do?")
    for i, animal in enumerate(at_the_zoo):
        print(f"{i + 1}. Visit {animal}")
    print(f"{len(at_the_zoo) + 1}. Exit")

    while not choise:
        try:
            choise = int(input("Enter your choice: \n"))
            if choise not in range(1, len(at_the_zoo) + 2):
                choise = 0
                print("Please enter a valid number")
            # choise = 0 if choise not in range(1, len(at_the_zoo) + 2) else choise or print("Please enter a valid number")

        except ValueError:
            print("Please enter a valid number")

    return choise

def main():
    in_zoo = True
    the_lions, the_elephants, the_giraffes = init_animals()

    print("Welcome to the Zoo!")
    visitor_name = input("What is your name: \n")
    visitor_age = 0

    while not visitor_age:
        try:
            visitor_age = abs(int(input("What is your age: \n")))
        except ValueError:
            print("Please enter a valid number")

    visitor = Visitor(visitor_name, visitor_age)
    print(visitor)
    
    # visitor = Visitor("visitor_name", 6)

    while in_zoo:
        do_in_zoo = show_menu(at_the_zoo)
        match do_in_zoo:
            case 1:
                visit_animal(the_lions, "lions", visitor, animal_food)
            case 2:
                visit_animal(the_elephants, "elephants", visitor, animal_food)
                
            case 3:
                visit_animal(the_giraffes, "giraffes", visitor, animal_food)
            case 4:
                print("Visiting all the animals")
                if not the_lions and not the_elephants and not the_giraffes:
                    print("There are no animals in the zoo, they all died")
                    continue
                for animal in the_lions + the_elephants + the_giraffes: 
                    if animal.energy <= 25:
                        print(f"{animal.get_name()} is sleeping.")
                        animal.sleep()
                        continue
                    
                    if animal.use_energy():
                        if animal.get_name() in [animal.get_name() for animal in the_lions]:
                            the_lions.remove(animal) 
                        elif animal.get_name() in [animal.get_name() for animal in the_elephants]:
                            the_elephants.remove(animal) 
                        elif animal.get_name() in [animal.get_name() for animal in the_giraffes]:
                            the_giraffes.remove(animal) 
                
                for animal in the_lions + the_elephants + the_giraffes:
                    print(animal)

                look_closer = input("Look closer? enter ('yes' or 'no') \n").lower()
                
                while not look_closer in ["yes", "y", "no", "n"]:
                    look_closer = input("Please enter 'yes' or 'no'")

                if look_closer in ["yes", "y"]:
                    two_animals = random.sample(the_lions + the_elephants + the_giraffes, 2)
                    print(f"{visitor.get_name()} is watching {two_animals[0].get_name()} and {two_animals[1].get_name()} interact")
                    input("Press enter to continue to see the interaction...")
                    animal_interaction(two_animals)
                    for animal in two_animals:
                        if animal.use_energy(0):
                            if animal.get_name() in [animal.get_name() for animal in the_lions]:
                                the_lions.remove(animal) 
                            elif animal.get_name() in [animal.get_name() for animal in the_elephants]:
                                the_elephants.remove(animal) 
                            elif animal.get_name() in [animal.get_name() for animal in the_giraffes]:
                                the_giraffes.remove(animal)
                    input("Press enter to continue")
                else:
                    print("What would you like to do now?")

            case 5:
                in_zoo = False
            case _:
                print("Please enter a valid number")


if __name__ == "__main__":
    main()