""" Dice program
    user>computer user wins
    computer>user computer wins
    user=computer roll again
"""

import random
def ucom():
    user=int(input())
    com=random.randrange(1,7)
    print(com)
    ans(user,com)
def ans(user,com):
    if(user==com):
        ucom()
    elif(user>com):
        print("winner")
    else:
        print("looser")
ucom()
