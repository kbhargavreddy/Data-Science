""" Dice program
    user>computer user wins
    computer>user computer wins
    user=computer roll again
"""

import random
while(True):
  user=int(input(""))
  computer=random.randint(1,6)
  print(computer)
  if(user>computer):
    print("User wins")
    break
  elif(user<computer):
    print("Computer wins")
    break
  else:
    print("Roll again")
    pass