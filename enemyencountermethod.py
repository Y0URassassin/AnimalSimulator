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