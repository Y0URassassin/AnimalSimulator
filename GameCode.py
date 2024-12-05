import random
import time
import os
from playsound import playsound

#clears screen learned from https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    os.system('cls')

#function to quickly pause the game until ENTER is pressed
def hold():
    time.sleep(.5)
    print()
    input("Press ENTER to continue.")
    clear()

#player class holds all player statistics and action menu methods
class Player():
    def __init__(self, name, energy, food, offspring):
        self.name = name.upper()
        self.energy = energy
        self.nearbyfood = food
        self.offspring = offspring

    #shows current player stats
    def playerCheck(self):
        print("ENERGY:", self.energy)
        print("OFFSPRING:", self.offspring, "of a possible 6.")

    #default actions shown here (no weather or enemy event)
    def actionReg(self):
        player_ans = input(f"What do you want to do?\n"
                           f"(1)  |migrate     |  [-2 ENERGY]\n"
                           f"(2)  |hunt        |  [+/-1 ENERGY]\n"
                           f"(3)  |lay egg     |  [-5 ENERGY]\n"
                           f"(4)  |eat baby    |  [-1 OFFSPRING] [+3 ENERGY]\n"
                            f"CHOICE:")

        #MIGRATE
        clear()
        if player_ans == "1":
            print(self.name, "migrates to a new place. (-2 ENERGY)")
            self.energy -= 2
            self.nearbyfood += random.randrange(1,6)

        #HUNT
        elif player_ans == "2":
            if self.nearbyfood > 0:
                print(self.name, "found some food to eat. (+1 ENERGY)")
                self.nearbyfood -= 1
                self.energy += 1
            elif self.nearbyfood <= 0:
                print(self.name, "couldn't find food. (-1 ENERGY)")
                self.energy-=1

        #OFFSPRING CODE - LAY EGG
        elif player_ans == "3":
            if self.energy > 5 and self.offspring < 6:
                self.offspring += 1
                self.energy -= 5
                print(self.name, "laid an egg. (-5 ENERGY) (+1 OFFSPRING)")
            else:
                print(self.name, "cannot lay an egg at this time.")

        #OFFSPRING CODE - EAT BABY
        elif player_ans == "4":
            if self.offspring > 0:
                print(self.name, "did what they had to survive. (-1 OFFSPRING) (+3 ENERGY)")
                self.energy += 3
                self.offspring -= 1
            elif self.offspring <= 0:
                print("No OFFSPRING to eat.")

        else:
            print(self.name, "chose to waste time (-1 ENERGY)")
            self.energy -= 1
        hold()


#Logic for enemy encounter
    def actionEnemy(self):
        print()
        player_ans = input(f"What do you want to do?\n"
                           f"(1)  |run      |  [-2 ENERGY]\n"
                           f"(2)  |fight    |  [+/-4 ENERGY]\n"
                           f"(3)  |sacrifice|  [-1 OFFSPRING]\n"
                            f"CHOICE:")
        clear()
        if player_ans == "2":
            randnum = random.randrange(0,2)
            if randnum == 1:
                self.energy += 4
                print(self.name, "won the fight! (+4 ENERGY)")
            elif randnum == 0:
                self.energy -= 4
                print(self.name, "lost the fight! (-4 ENERGY)")
        elif player_ans == "3":
            if self.offspring <= 0:
                print(self.name, "Has no OFFSPRING to sacrifice.")
                self.energy -= 2
                print(self.name, "ran away. (-2 ENERGY)")
            elif self.offspring > 0:
                self.offspring -=1
                print(self.name, "gave up their OFFSPRING to escape safely. (-1 OFFSPRING)")
            else:
                self.energy -= 2
                print(self.name, "ran away. (-2 ENERGY)")
        else:
            self.energy -= 2
            print(self.name, "ran away. (-2 ENERGY)")
        hold()

    #Logic for random weather events and hiding
    def actionWeather(self):
        print()
        location_list = ["Bushes","Rock","Cave","Trees","Sand","Ground","Log",]
        success_list = [random.randrange(0,2),random.randrange(0,2)]
        player_ans_list = [0,0]
        print("Where do you want to hide?")
        print("(1)  |", location_list[random.randrange(0,7)],"|")
        print(f"(2)  |", location_list[random.randrange(0,7)],"|")
        player_ans = input("CHOICE:")
        clear()
        if player_ans == "1":
            player_ans_list[0] = 1
            if player_ans_list[0] == success_list[1]:
                print(self.name, "found a safe place to weather the storm.")
            else:
                print(self.name, "was unable to escape the weather. (-1 ENERGY)")
                self.energy -= 1

        elif player_ans == "2":
            player_ans_list[1] = 1
            if player_ans_list[1] == success_list[1]:
                print(self.name,"found a safe place to weather the storm.")
            else:
                print(self.name, "was unable to escape the weather. (-1 ENERGY)")
                self.energy -= 1

        else:
            print(self.name, "was unable to escape the weather. (-1 ENERGY)")
            self.energy -= 1
        hold()

#allows player to decide how long the game should go on for.
def pickGameLength():
    clear()
    print("Pick a game length:")
    print()
    int_gmode = input(f"(1) day\n"
                     f"(2) week (recommended)\n"
                     f"(3) month\n"
                     f"CHOICE:")
    if int_gmode == "1":
        return 1
    elif int_gmode == "2":
        return 7
    elif int_gmode == "3":
        return 30
    else:
        return 7

def instructions():
    clear()
    print(f"You will be an animal.\n"
          f"Last for the number of days chosen to recieve an ANIMAL SCORE.\n"
          f"Gain energy, make babies.\n"
          f"If you run out of energy, you will die.\n")
    hold()
    titleScreen()

def gameLoss():
    clear()
    playsound("death.wav")
    print(player.name, "has died!")
    again = input("Play again? (Y/N):")
    if again == "y" or again == "Y":
        gameStart(titleScreen())
    else:
        exit()

def animalScore():
    if player.offspring == 0:
        anscore = player.energy * (1 + player.offspring)
    else:
        anscore = player.energy * player.offspring
    if anscore > 100:
        anscore == 100
    elif anscore < 0:
        anscore == 0
    return anscore


def gameWin():
    try:
        playsound("success.wav")
    except:
        print("ERROR: sound not playable!")
    clear()
    print(player.name, "survived!")
    time.sleep(1)
    print("ENERGY gained:       |", player.energy)
    time.sleep(1)
    print("OFFSPRING multiplier:|", (player.offspring + 1))
    time.sleep(1)
    print("ANIMAL SCORE:        |", animalScore())
    print()

    save = input("Save Score? (Y/N):")
    if save == "y" or save == "Y":
        try:
            score_file = open("score.txt","w+")
            score_file.write(str(animalScore()))
            score_file.close()
        except:
            score_file = open("score.txt","x")
            score_file.close()
            score_file = open("score.txt","w+")
            score_file.write(str(animalScore()))
            score_file.close()

    again = input("Play again? (Y/N):")
    if again == "y" or again == "Y":
        gameStart(titleScreen())
    else:
        exit()

def selectEvent():
    #Events 1 thru 6 should be standard; 7 thru 10 should be unique (weather, enemy, etc.)
    event = random.randrange(1,11)
    return event

# the gameplay starts here.
def gameDay(length):
    clear()
    if length == None:
        length = 7
    for currentday in range(length):
        hours = 12
        print("It is the dawn of day {}.\n".format(currentday + 1))
        time.sleep(2)
        # 1 thru 6 triggers standard action event, rest are special cases (weather/enemy)
        event_prompt_dict = {1: "",
                             2: "",
                             3: "",
                             4: "",
                             5: "",
                             6: "",
                             7: "A bad storm is approaching!",
                             8: "A bad storm is approaching!",
                             9: "An enemy animal is approaching!",
                             10: "An enemy animal is approaching!",
                             }
        for i in range(hours):
            if player.energy <= 0:
                gameLoss()
            clear()
            print("Hours remaining:", hours,"\n")
            hours -= 1
            player.playerCheck()
            event = selectEvent()
            print(event_prompt_dict[event])
            print()
            if event == 1 or event == 2 or event == 3 or event == 4 or event == 5 or event == 6:
                player.actionReg()
            elif event == 7 or event == 8:
                player.actionWeather()
            elif event == 9 or event == 10:
                player.actionEnemy()

    #day ends, run random end-of-day events and show player stats
        clear()
        print("The day has ended.")
        print()
        chance_event = random.randrange(0,5)
        if chance_event == 0:
            player.energy += 1 * (player.offspring // 2)
            print (player.name, "sleeps peacefully. (+",1+ 1 * (player.offspring // 2)," ENERGY)")
            print()

        elif chance_event == 1:
            player.energy -= 1 * player.offspring
            print (player.name, "sleeps poorly. (-",1+1 * player.offspring," ENERGY)")
            print()

        elif chance_event == 3:
            if player.offspring > 0:
                player.offspring -= 1
                print("1 OFFSPRING was lost last night.")
                print(player.name, "now has", player.offspring, "OFFSPRING remaining.")
            else:
                print(player.name, "sleeps.")
                print()

        else:
            print(player.name, "sleeps.")
            print()

        player.energy += int(player.offspring) * 2
        print(player.name, "'s OFFSPRING increased", player.name, "'s ENERGY by", int(player.offspring)* 2,".")
        print()

        if player.energy <= 0:
            gameLoss()
        player.playerCheck()
        hold()
    gameWin()

#function to initialize player variable as a Player class and call gameDay() to start the game
def gameStart(length):
    if length == None:
        length = 7
    clear()
    global player
    player = Player(input("Name your animal:"), random.randrange(5,9), random.randrange(2,7), random.randrange(0,2))
    clear()
    print(f"You are", player.name,".\n"
          f"Survive for", length, "day(s) to recieve your ANIMAL SCORE.\n")
    hold()
    gameDay(length)

#show previous score on title screen, gives player choice to start game or read instructions
def titleScreen():
    clear()
    print("|================|")
    print("|ANIMAL SIMULATOR|")
    print("|================|")
    print("By Zachary Fernandes, Dawson Clark, and Nolan Zimmerman.")
    print()

    try:
        high_score = open("score.txt","r")
        hsprint = high_score.read()
        print("Previous Score:", hsprint)
        high_score.close()
    except:
        print("Previous Score: 0")

    playsound("gamestart.wav")
    print()
    print(f"\n(1) START GAME\n"
          f"(2) INFORMATION")

    choice = input("CHOICE:")
    if choice == "1":
        return pickGameLength()
    else:
        instructions()

gameStart(titleScreen())


