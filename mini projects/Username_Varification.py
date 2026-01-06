#  Rules -
#  The username must not be longer than 12 characters
#  The username mudt not contain spaces
#  The username must not contain digits.

Username = input("Enter you Username:  ")

test1 = len(Username)
test3 = Username.find(" ")
test2 = Username.isalpha
if test1 > 12:
  print("your username must be no longer than 12 characters!")
elif test3 != -1:
  print("Your user Name must not have any spaces!")
elif test2 == False:
  print("Your username can not have numbers in it!")
else:
  print(f"Welcome {Username}")

  
