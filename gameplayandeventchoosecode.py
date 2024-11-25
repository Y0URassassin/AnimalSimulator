import random
import time
import os
from playsound import playsound

def selectEvent():
    #Events 1 thru 6 should be standard; 7 thru 10 should be unique (weather, enemy, etc.)
    event = random.randrange(1,11)
    return event

# the gameplay starts here.
def gameDay(length):
    clear()
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
    clear()
    global player
    player = Player(input("Name your animal:"), random.randrange(5,9), random.randrange(2,7), random.randrange(0,2))
    clear()
    print(f"You are", player.name,".\n"
          f"Survive for", length, "day(s) to recieve your ANIMAL SCORE.\n")
    hold()
    gameDay(length)


