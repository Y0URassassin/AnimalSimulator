# default actions shown here (no weather or enemy event)
def actionReg(self):
    player_ans = input(f"What do you want to do?\n"
                       f"(1)  |migrate     |  [-2 ENERGY]\n"
                       f"(2)  |hunt        |  [+/-1 ENERGY]\n"
                       f"(3)  |lay egg     |  [-5 ENERGY]\n"
                       f"(4)  |eat baby    |  [-1 OFFSPRING] [+3 ENERGY]\n"
                       f"CHOICE:")

    # MIGRATE
    clear()
    if player_ans == "1":
        print(self.name, "migrates to a new place. (-2 ENERGY)")
        self.energy -= 2
        self.nearbyfood += random.randrange(1, 6)

    # HUNT
    elif player_ans == "2":
        if self.nearbyfood > 0:
            print(self.name, "found some food to eat. (+1 ENERGY)")
            self.nearbyfood -= 1
            self.energy += 1
        elif self.nearbyfood <= 0:
            print(self.name, "couldn't find food. (-1 ENERGY)")
            self.energy -= 1

    # OFFSPRING CODE - LAY EGG
    elif player_ans == "3":
        if self.energy > 5 and self.offspring < 6:
            self.offspring += 1
            self.energy -= 5
            print(self.name, "laid an egg. (-5 ENERGY) (+1 OFFSPRING)")
        else:
            print(self.name, "cannot lay an egg at this time.")

    # OFFSPRING CODE - EAT BABY
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