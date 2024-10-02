# 1. Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
def calculates():
    base = int(input('Enter the base '))
    exponent = int(input('Enter the exponent '))

    result = 1
    for i in range(exponent):
        result *= base

    return result
    
# 2. Write a program that calculates the sum of all elements in a given tuple.
def sum_of_elements():
    my_tuple = (1, 2, 3, 4, 5)

    return sum(my_tuple)

# 3. Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
def even_numbers():
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    even = tuple([num for num in my_tuple if num % 2 == 0])

    return even

# 4. Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the value from the second dictionary should be used.
# Exemple 1
def merge_dicts():
    dict1 = {'a': 1, 'b': 2, 'c':3, 'd': 4}
    dict2 = {'b': 3, 'c': 4, 'd': 5, 'e': 6}
    new_dict = {}

    new_dict.update(dict1)
    new_dict.update(dict2)

    return new_dict

# Exemple 2
def merge_dicts2():
    dict1 = {'a': 1, 'b': 2, 'c':3, 'd': 4}
    dict2 = {'b': 3, 'c': 4, 'd': 5, 'e': 6}
    new_dict = dict1.copy()

    for key, value in dict2.items():
        new_dict[key] = value

    return new_dict

# 5. Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.
def even_number():
    user_input = input("Enter a list of integers separated by spaces: ")

    integer_list = [int(num) for num in user_input.split()]

    even_nums = [num for num in integer_list if num % 2 == 0 ]

    return even_nums

# 6. Write a program that takes a string as input and prints its reverse.
def reverse_input():
    user_input = input("Enter the string that you want to have reversed:\n ")

    return user_input[::-1]




labs_list = [
    '1. The power calculater', 
    '2. The sum of Tuple', 
    '3. Even numbers of Tuple', 
    '4. Merge 2 dictionaries', 
    '5. The list comprehension',
    '6. Reverse the string'
]

def started_lab():
    in_lab = True

    while in_lab:
        for title in labs_list:
            print(title)
        print('')

        command = input('Enter the corresponding number of lab ')

        match command:
            case '1':
                print(calculates())
            case '2':
                print(sum_of_elements())
            case '3':
                print(even_numbers())
            case '4':
                print(merge_dicts2())
            case '5':
                print(even_number())
            case '6':
                print(reverse_input())
            case _:
                print("Unknown command Try again.")

        while True:
            continue_input = input("Enter 'True' to continue or 'False' to quit: ").strip().lower()
            if continue_input in ["true", "false"]:
                in_lab = continue_input == "true"
                break
            else:
                print("Invalid input, please enter 'True' or 'False'.")
        print('')


started_lab()