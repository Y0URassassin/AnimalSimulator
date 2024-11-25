def actionWeather(self):
    print()
    location_list = ["Bushes", "Rock", "Cave", "Trees", "Sand", "Ground", "Log", ]
    success_list = [random.randrange(0, 2), random.randrange(0, 2)]
    player_ans_list = [0, 0]
    print("Where do you want to hide?")
    print("(1)  |", location_list[random.randrange(0, 7)], "|")
    print(f"(2)  |", location_list[random.randrange(0, 7)], "|")
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
            print(self.name, "found a safe place to weather the storm.")
        else:
            print(self.name, "was unable to escape the weather. (-1 ENERGY)")
            self.energy -= 1

    else:
        print(self.name, "was unable to escape the weather. (-1 ENERGY)")
        self.energy -= 1
    hold()
