import math, random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.constitutionModifier = modifier(self.constitution)
        self.hitpoints = self.constitutionModifier + 10
    def ability(self):
        vals = [random.randint(1,6) for i in range(4)]
        return sum(vals) - min(vals)

def modifier(constituionValue):
    return math.floor((constituionValue -10) / 2)