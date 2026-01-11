#  Advance Shopping Cart 

foods = []
prices = []
total = 0

while True:
  food = input("Add Food to cart (q or e to quit):  ")
  if food.lower() == "q" or food.lower() == "e":
    print("Shopping completed ✅")
    break 
  else:
    vowels = "aeiou" #just so english doesn't haunt me forever 
    article = "an" if food[0].lower() in vowels else "a"
    price = float(input(f"Enter the value of {article} {food}:  ₹"))
    foods.append(food)
    prices.append(price)

print("------------YOUR CART--------------")

for food in foods:
  print(food)

for price in prices:
  total += price
  
print()
print(f"Your total would be {total}₹")