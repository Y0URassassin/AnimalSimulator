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
    playsound("instructions.wav")
    print(f"You will be an animal.\n"
          f"Last for the number of days chosen to recieve an ANIMAL SCORE.\n"
          f"Gain energy, make babies.\n"
          f"If you run out of energy, you will die.\n")
    hold()
    titleScreen()
