print("Welcome to Treasure Island")
print("--------------------------\n\n")
gate1 = input('In fornt of you there is 3 gates to continue, which one do you choose "left" "right" and "straight" ?.\n')
if gate1 == "right":
  print("You are wrong way, game over")
elif gate1 == "left":
  print("You are back to previous gate")
elif gate1 == "straight":
  print("Next Gate is open")
  gate2 = input('There is 3 gate again choose "1","2","3" \n')
  if int(gate2) == 1:
    print("You are fall to the water")
  elif int(gate2) == 2:
    print("Gate open, There is 2 cables here you have to cut off")
    gate3 = input('Choose "yellow" or "red" if wrong, you are died\n')
    if gate3 == "red":
      print("You win")
    elif gate3 == "yellow":
      print("Booooom the bomb explode, Game over")
    else:
      print("Game over")
  else:
      print("Game over")
else:
  print("wrong way, Game over")
  
