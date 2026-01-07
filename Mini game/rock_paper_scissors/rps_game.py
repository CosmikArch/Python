#  rock paper scissors

import random #  for choice computers can't think duh 🙄 
import time #  for the countdown 🙂 

Greeting = ["I foresee a future, where you lose!", "I foresee a future where victory is you destiny!", "You walked have upon the path of misry, now suffer!", "Your path may lead you to victory!","Feeling lucky, aren't you?", "I hope you don't regret your choices!"] #  i still haven't learned about lists and truples much (i believe i spelt that wrong )

Greet = random.choice(Greeting) #Dont' get scared now

player = input("Enter your username:  ") #please don't use numbers 🥺

print(f"Greeting, {player}, I am RNG_The_Chad. {Greet}")

choices = ["rock", "paper", "scissors"] #actual set of choices

computer_choice = random.choice(choices) #to randomly pick ⛏️ a set choice 

print("Rock") #a count down for more realism
time.sleep(0.5)
print("paper")
time.sleep(0.5)
print("scissors")
time.sleep(0.5)

player_choice  = input("Choose you call:  ")
player_choice = player_choice.lower()

time.sleep(1)
print(f"RNG_The_Chad chose {computer_choice}") # to actually see what The Chad chose

#  tie condition 
if player_choice == computer_choice:
  print("It's a tie!")
  
#  winning conditions
elif player_choice == "rock" and computer_choice == "scissors":
  print("You win!🎊")
elif player_choice == "paper" and computer_choice == "rock":
  print("You win!🎉")
elif player_choice == "scissors" and computer_choice == "paper":
  print("You win!🎉") #winning conditions done ✅
  
  #  loosing conditions
elif player_choice == "rock" and computer_choice == "paper":
  print("You lose! :(")
elif player_choice == "paper" and computer_choice == "scissors":
  print("You lose! :(")
elif player_choice == "scissors" and computer_choice == "rock":
  print("You lose! :(")
  
else:
  print(f"{player_choice} is not a valid choice! you are dumb 🗿")
