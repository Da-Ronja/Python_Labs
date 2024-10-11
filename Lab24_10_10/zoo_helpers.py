# zoo.helpers.py
from Animal import low_energy

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
        except ValueError:
            print("Please enter a valid number")

    return choise

def look_at_animals():
    print("You can look at all animals or just one")
    user_input = ""
    while not user_input in ["all", "one"]:
        user_input = input("Would you like to look at all animals or just one? (all/one): \n").lower()
        if user_input not in ["all", "one"]:
            print("Please enter 'all' or 'one'")
    
    return user_input

def if_all_animals(list_of_animals):
    for animal in list_of_animals:
        print(animal)
        if animal.use_energy():
            list_of_animals.remove(animal)
            print(f"{animal.get_name()} has died")
    return list_of_animals


def choose_animal(list_of_animals):
    user_input = 0
    while not user_input in range(1, len(list_of_animals) + 1):
        try:
            for i, animal in enumerate(list_of_animals):
                print(f"{i + 1}. {animal.get_name()}")
            user_input = int(input("Which animal would you like to visit? \n"))
            if user_input not in range(1, len(list_of_animals) + 1):
                user_input = 0
                print("Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")
    return list_of_animals[user_input - 1]

def look_or_feed():
    user_input = ""
    while not user_input in ["look", "feed"]:
        user_input = input("Would you like to look at the animal or feed it? (look/feed): \n").lower()
        if user_input not in ["look", "feed"]:
            print("Please enter 'look' or 'feed'")
    return user_input

def feed_one_animal(animal_food):
    food_choise = 0
    while not food_choise in range(1, len(animal_food) + 1):
        try:
            for i, food in enumerate(animal_food):
                print(f"{i + 1}. {food}")
            food_choise = int(input("What would you like to feed the animal? \n"))
            if food_choise not in range(1, len(animal_food) + 1):
                food_choise = 0
                print("Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")
    return food_choise

def visit_animal(animal_list, animal_type, visitor, animal_food):
    if not animal_list:
        print(f"There are no {animal_type} in the zoo. They all died")
        return animal_list

    print(f"Visiting the {animal_type}")
    look_at = look_at_animals()

    if look_at == "all":
        animal_list = if_all_animals(animal_list)
        input("Press enter to continue")
    elif look_at == "one":
        animal = choose_animal(animal_list)
        print(f"Visiting {animal.get_name()}")

        if low_energy(animal):
            return animal_list

        do = look_or_feed()
        if do == "feed":
            food = feed_one_animal(animal_food)
            visitor.feed(animal, animal_food[food - 1])
        else:
            visitor.visit(animal)
        input("Press enter to continue")

        if animal.use_energy():
            animal_list.remove(animal)
    return animal_list