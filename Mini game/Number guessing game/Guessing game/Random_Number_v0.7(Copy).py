#  number guessing game

import random

print("Random Number Guessing Game V0.8")

player = input("Enter your Username:  ")
print(f"Hello {player}")

win = 0
losses = 0

print("-----------------------------------------------------------")

while True:
  num = random.randint(1, 9)
  
  guess = int(input("pick a number from 1 to 9:  "))
  if guess == num:
    print("You won!! :3")
    win += 1
  else:
    print(f"You lose!! The number actually was {num} Try again :(")
    losses += 1
  
  print(f"""|—————current Score——————|
   {player}: {win}
   RNG_The_Chad: {losses}""")
  
  if win == 3:
    print("RNG_The_Chad: You are lucky aren't you? but for not long! 👿")
  
  if losses == 3:
    print("RNG_The_Chad: You suck at this buddy! 😈")

  if win == losses:
    print("Something bad, bad is about to happen!")
  
  if win >= 5:
    print("RNG_The_Chad: I guess you won!! but next time you will not! 🗿")
    Option = input("Do you want to play again? (y/n):  ")
    if Option.lower() == "y":
      win = 0
      losses = 0
      continue
    elif Option.lower() == "n":
      break
    else:
      print('Invalid Choice! try again')
      continue 
    
  if losses >= 5:
    print(F"RNG_The_Chad: You lost by {win} - {losses} You suck buddy! Try again but i won't go easy!!")
    Option = input("Do you want to play again? (y/n):  ")
    if Option.lower() == "y":
      win = 0
      losses = 0
      continue
    elif Option.lower() == "n":
      break
    else:
      print('Invalid Choice! try again')
      continue 
