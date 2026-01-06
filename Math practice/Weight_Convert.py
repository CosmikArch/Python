# python weight converter

weight = float(input("Enter your weight:  "))
Unit = input("Choose An unit (K for Kilograms/ L for pounds):  ")

if Unit == "K":
  lbs = weight * 2.20462
  print(f"Your weight is {round(lbs, 2)} lbs.")
  
elif Unit == "L":
  kgs = weight / 2.20462
  print(f"your weight is {round(kgs, 1)} kgs")
 
else:
	print(f"Unit {Unit} is not vaild(try K or L)")


