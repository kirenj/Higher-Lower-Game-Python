from art import logo
from art import vs
import random
from game_data import data
from replit import clear

COMP_A = 0
COMP_B = 0
USER_SELECTION = ""

def comparison_A(number):
  name = data[number]["name"]
  description = data[number]["description"]
  country = data[number]["country"]
  followers = data[number]["follower_count"]  
  print(f"Compare A: {name}, a {description}, from {country}")
  return followers

def comparison_B(number):
  name = data[number]["name"]
  description = data[number]["description"]
  country = data[number]["country"]
  followers = data[number]["follower_count"]  
  print(f"Against B: {name}, a {description}, from {country}")
  return followers

def check():
  dict = {
    "a": COMP_A,
    "b": COMP_B
  }
  if USER_SELECTION == 'a':
    if dict["a"] > dict["b"]:
      return True
    else:
      return False
  elif USER_SELECTION == 'b':
    if dict["b"] > dict["a"]:
      return True
    else:
      return False


def game():
  global COMP_A
  global COMP_B
  global USER_SELECTION
  
  print (logo)
  
  continue_game = True
  score = 0
  random_number_A = int(random.randint(0, len(data) - 1))
  random_number_B = int(random.randint(0, len(data) - 1))
  if random_number_A == random_number_B:
    random_number_B = int(random.randint(0, len(data) - 1))
  
  while continue_game == True:
    
    # print(f"The random number A is {random_number_A}")
    # print(f"The random number B is {random_number_B}")
    
    COMP_A = comparison_A(random_number_A)
    print(vs)
    COMP_B = comparison_B(random_number_B)
  
    # print(f"The follower count of A is {COMP_A}")
    # print(f"The follower count of B is {COMP_B}")
    
    USER_SELECTION = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    check_value = check()
    
    if check_value == True:
      score += 1
      random_number_A = random_number_B
      random_number_B = int(random.randint(0, len(data) - 1))
      clear()
      print(f"You're right! Current score: {score}")
      continue_game = True
    else:
      clear()
      print(f"Sorry, that's wrong. Final score: {score}")
      continue_game = False


game()

