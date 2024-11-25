import random
from random import choice
import time
import os
from playsound import playsound


def actionEnemy():
    player_ans = int(input(f"What do you want to do?\n"
                       f"(1)  |run      |  [-2 ENERGY]\n"
                       f"(2)  |fight    |  [+/-4 ENERGY]\n"
                       f"(3)  |sacrifice|  [-1 OFFSPRING]\n"
                        f"CHOICE:"))
    try:
        if player_ans == 1:
            print("ran away. (-2 ENERGY)")
        elif player_ans == 2:
            randnum = random.randrange(0,2)
            print(randnum)
            if randnum == 0:
                print("won the fight! (+4 ENERGY)")
            elif randnum == 1:
                print("lost the fight! (-4 ENERGY)")
        else:
            print("ran away")
    except ValueError:
        print("ran away. (-2 ENERGY)")




#actionEnemy()
#time.sleep(2)
#test for new menu fix
reg = input("this is a test of the string inputs as choices instead:")
if reg == "0":
    print("ZERO")
elif reg == "1":
    print("ONE")
else:
    print("ELSE!!")