import random
playing = True
number = str(random.randint(0,12))

print("I will choose a number 0 to 12, your job is to guss the number on digit at once")
print("The game end when you gussed it properly")

while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
      print("Victory")
      print("Wasted",number)
      break
  
    else:
      print("to close give another try, \n")