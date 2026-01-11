#  Advance Shopping Cart 

foods = []
prices = []
quantities = []
total = 0

while True:
  food = input("Add Food to cart (q or e to quit):  ")
  if food.lower() == "q" or food.lower() == "e":
    print("Shopping completed ✅")
    break 
  else:
    price = float(input(f"What is the price of 1 {food}:  ₹"))
    quantity = int(input(f"how many {food} are you buying?  "))
    price = price * quantity 
    
    foods.append(food)
    prices.append(price)
print("------------YOUR CART--------------")

for i in range(len(foods)):
    print(f"{foods[i]} : ₹{prices[i]}")

total = sum(prices)

print("--------------------------------------------")
print(f"Your total would be ₹{total}")
