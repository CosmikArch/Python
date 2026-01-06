import math

a = int(input("Enter the length of the side A:  "))
b = int(input("Enter the length of the side B:  "))

c = math.sqrt(pow(a, 2) + pow(b,2))

print(f"the length of the hypotenuse of the triangle is: {round(c, 3)}")