import random
# number guess game
print("Welcome to guess number game")
player_number = input("Entre a number between 0 - 10 : ")

# computer random number 

computer_number = random.randrange(0, 10)
# check the numbers
def check(player, computer) :
  if int(player) == computer :
    return "you won"
  else :
    return "You lost"
print(check(player_number, computer_number))
print("The computer has selected number : {}".format(computer_number))
