class Character:
    def __init__(self, name, age, strength, agi, con, race, damage):
        self.name = name
        self.age = age
        self.strength = strength
        self.agi = agi
        self.con = con * 10
        self.race = race
        self.damage = damage
        self.dead = False
        self.exp = 0
        self.exp_to_next_level = 50
        self.level = 1

    def damage_received(self, damage):
        self.con -= damage
        if self.con <= 0:
            self.dead = True

    def damage_send(self, sum_dice):
        if 2 <= sum_dice <= 4:
            self.damage += 1
        elif 5 <= sum_dice <= 7:
            self.damage += 2
        elif 8 <= sum_dice <= 10:
            self.damage += 3
        elif sum_dice == 11:
            self.damage += 4
        elif sum_dice == 12:
            self.damage += 5
        return self.damage

    def check_to_next_level(self):
        if self.exp >= self.exp_to_next_level:
            self.level += 1
            self.exp = 0
            self.exp_to_next_level *= 1.5
            self.strength *= 1.1
            self.agi *= 1.1
            self.con *= 1.1
            self.damage = self.strength / 3
            print(f"{self.name} Subio de nivel")
            print(self.damage)