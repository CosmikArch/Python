#  this is a basic temperature converter i coded at mid night 2:29am
 #  don't expect it to work i am hungry and sleepy 
 #  Version 0.1
import time 
import random

roasts = [
    # Brutal
    "That input wasn’t a number. Python refused it like a bad thesis.",
    "I asked for a temperature. You gave me disappointment.",
    "Numbers have structure. This had vibes.",
    
    # Psychological
    "This input suggests confusion, hesitation, and unchecked optimism.",
    "Somewhere inside you knew this wouldn’t work. You typed it anyway.",
    "This is not a mistake. This is a pattern.",
    
    # Philosophical
    "You entered a symbol where meaning was required.",
    "Plato warned us about forms like this.",
    "Is this input real, or merely a shadow of a number on the cave wall?",
    
    # Scientific
    "Scientifically speaking, that is not a measurable quantity.",
    "This input violates basic numerical integrity.",
    "Even experimental error has limits.",
    
    # Thermodynamic
    "Entropy increased the moment you pressed Enter.",
    "This input has negative usefulness and positive chaos.",
    "No known thermodynamic process converts this into a float.",
    
    # Astrophysical
    "In an infinite universe, this is still not a number.",
    "Black holes accept everything. Python does not.",
    "Even cosmic background radiation makes more sense than this.",
    
    # Programmer-specific cruelty
    "float() tried. It really did.",
    "Python didn’t crash. It chose self-respect.",
    "This is why exceptions exist. And why mentors sigh.",
    
    # Existential finisher
    "The machine asked for clarity. You answered with mystery.",
    "This input will be remembered. Not fondly.",
    "Somewhere, a compiler weeps.","That wasn't a number. Python is confused and so am I 💀",
    "Interesting choice. Unfortunately, numbers exist.",
    "You typed a letter. This is a temperature converter, not Scrabble.",
    "I asked for a number, not your blood type.",
    "Python tried to convert that and immediately gave up."
]
print("""Basic temperature converter 
(supports only Celsius and fahrenheit)""")
print("Note- The unit in operation is to choose that conversion unit not to state the initial unit")

while True:
    unit = input("Choose an operation (C/F/Q): ").lower()

    if unit == "q":
        print("Stopping converter........")
        break

    time.sleep(2)

    try:
        temp1 = float(input("Enter the Temperature: "))
    except ValueError:
      time.sleep(1.5)
      print(random.choice(roasts))
      continue

    if unit == "f":
        print(f"{temp1}°C in Fahrenheit is {round((temp1 * 9/5) + 32, 3)}°F")
    elif unit == "c":
        print(f"{temp1}°F in Celsius is {round((temp1 - 32) * 5/9, 3)}°C")
    else:
        print("Bro choose C, F, or Q. I'm not a mind reader.")