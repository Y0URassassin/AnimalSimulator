import random
import time
import os
from playsound import playsound


# clears screen
def clear():
    os.system('cls')


# function to quickly pause the game until ENTER is pressed
def hold():
    time.sleep(.5)
    print()
    input("Press ENTER to continue.")
    clear()


# player class holds all player statistics and action menu methods
class Player():
    def __init__(self, name, energy, food, offspring):
        self.name = name.upper()
        self.energy = energy
        self.nearbyfood = food
        self.offspring = offspring

    # shows current player stats
    def playerCheck(self):
        print("ENERGY:", self.energy)
        print("OFFSPRING:", self.offspring, "of a possible 6.")

