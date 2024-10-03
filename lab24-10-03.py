# 1. Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.
# Example:
import random

def arrayCheck(nums):
  sequence = [1, 2, 3]
  
  for i in range(len(nums)):
    if nums[i:i + len(sequence)] == sequence:
      return True

  return False

a1 = arrayCheck([1, 1, 2, 3, 1]) # True
b1 = arrayCheck([1, 1, 2, 4, 1]) # False
c1 = arrayCheck([1, 1, 2, 1, 2, 3]) # True

# print(f'a = {a1} \nb = {b1} \nc = {c1}')

# 2. Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".
# Example:

def stringBits(str):
  new_str = str[::2]

  return new_str

a2 = stringBits('Hello') # 'Hlo'
b2 = stringBits('Hi') # 'H'
c2 = stringBits('Heeololeo') # 'Hello'

# print(f'Hello = {a2} \nHi = {b2} \nHeeololeo = {c2}')

#3. Given a string, return a string where for every char in the original,
# there are two chars.
def doubleChar(str):
  new_str = ''

  for i in range(len(str)):
    new_str += str[i]*2

  return new_str

a3 = doubleChar('The') # 'TThhee'
b3 = doubleChar('AAbb') # 'AAAAbbbb'
c3 = doubleChar('Hi-There') # 'HHii--TThheerree'

# print(f'The = {a3} \nAAbb = {b3} \nHi-There = {c3}')

# 4. Return the number of even integers in the given array/list.
# Examples:
def count_evens(num_list):
  even_amount = 0

  for num in num_list:
    if num % 2 == 0:
      even_amount += 1
  
  return even_amount

a4 = count_evens([2, 1, 2, 3, 4]) # 3
b4 = count_evens([2, 2, 0]) # 3
c4 = count_evens([1, 3, 5]) # 0

# print(f'a4 = {a4} \nb4 = {b4} \nc4 = {c4}')

# 5. Optional Lab:
# You can actually make a simple command line game. You could put together everything
# you've learned so far about Python. The game goes like this:
# 1. The computer will think of 3 digit number that has no repeating digits.
def computer_digit():
    digits = random.sample(range(10), 3)
    # digits = list(range(10))
    # random.shuffle(digits)
    # print(digits[:3])

    return digits

# 2. You will then guess a 3 digit number
def guess_input():
    while True:
        guess = input('Enter three single numbers separated by spaces.\n')
        guess = [int(num) for num in guess.split()]
        if len(guess) == 3 and all(isinstance(x, int) for x in guess):
            return guess
        else:
            print("Invalid input. Please enter exactly three unique numbers.")

# 3. The computer will then give back clues, the possible clues are:
#  Close: You've guessed a correct number but in the wrong position
#  Match: You've guessed a correct number in the correct position
#  Nope: You haven't guess any of the numbers correctly
def clues(comp, user):
    you_win = False
    while not you_win:
        matches = 0
        clues_list = []
    
        for i in range(len(comp)):

            if user[i] == comp[i]:
                clues_list.append("Match") 
                matches += 1
            elif user[i] in comp:
                clues_list.append("Close")
            else:
                clues_list.append("Nope")
                if i == len(comp) - 1 and all(clue == 'Nope' for clue in clues_list):
                    clues_list = "Nope: You haven't guess any of the numbers correctly"
                    
        print(clues_list)

        if matches == len(comp):
            print("You win, perfect match!")
            you_win = True
        else: 
            user = guess_input()
    

# 4. Based on these clues you will guess again until you break the code with a
#  perfect match!
# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:
# Try to figure out what this code is doing and how it might be useful to you
# import random
# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3])
# Another hint:
# guess = input("What is your guess? ")
# print(guess)
# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence?
def game():
  print('Welcome to the guessing game! Think you can outsmart the computer and guess its three secret numbers? Give it your best shot!')
  computer_digits = computer_digit()
  user_guess = guess_input()

  clues(computer_digits, user_guess)

game()