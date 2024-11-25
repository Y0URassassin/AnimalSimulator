def gameLoss():
    clear()
    playsound("death.mp3")
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
    playsound("success.wav")
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
