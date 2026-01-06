#  this is a basic temperature converter i coded at mid night 2:29am
 #  don't expect it to work i am hungry and sleepy 
 #  Version 0.1
import time 
 
print("""Basic temperature converter 
(supports only Celsius and fahrenheit)""")
print("Note- The unit in operation is to choose that conversion unit not to state the initial unit")

while True:
  print("_______________________________________________________________________________")
  
  unit = input("Choose an operation (C for celcius, F for fahrenheit, Q for exit):  ")
  if unit.lower() == "q":
    print("Stopping converter........")
    break
  time.sleep(2)
  temp1 = float(input("Enter the Temperature:  "))
  
  if unit.lower() == "f":
    temp2 = (temp1 * 9/5) + 32
    print(f"{temp1}°C in Fahrenheit is {round(temp2, 3)}°F")
  elif unit.lower() == "c":
    temp2 = (temp1 - 32) * 5/9
    print(f"{temp1}°F in celsius is {round(temp2, 3)}°C")
  else:
    print(f"{unit} is not an registered unit!")
    continue 
