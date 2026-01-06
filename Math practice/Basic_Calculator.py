#  this is a super basic calculator
#  don't expect much functionality 😓

operator = input("Choose an Operator type (+,-,×, or ÷):  ")
num1 = float(input("Enter the first number:  "))
num2 = float(input("Enter the second number:  "))

if operator == "+":
  result = round(num1 + num2, 4)
  print(F"{num1} + {num2} = {result}")
  
elif operator == "-":
  result = round(num1 - num2, 4)
  print(f"{num1} - {num2} = {result}")
  
elif operator == "×":
  result = round(num1 * num2, 4)
  print(f"{num1} × {num2} = {result}")
  
elif operator == "÷":
  if num2 != 0:
   result = round(num1/num2, 4)
   print(f"{num1} /{num2} = {result}")
   
else: 
  print("Invalid operator!")
