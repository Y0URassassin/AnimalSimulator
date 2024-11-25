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