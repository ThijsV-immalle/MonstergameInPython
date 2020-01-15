import random

class Creature:
    def getName(self):
        return self.name

    def getHP(self):
        return self.hp
    def setHP(self, value):
        self.hp = value

    def __init__(self, name, hp = 100, ap = 20):
        self.name = name
        self.hp = hp
        self.ap = ap

    def Attack(self, c):
        damage = random.randint(0, self.ap + 1)
        c.HP -= damage
        if c.HP <=0:
            print(f"{self.name} attacks {c.name} and does {damage} damage. {c.name} dies.")
            return True

        else:
             print(f"{self.name} attacks {c.name} and does {damage} damage. {c.name} now has {c.HP} HP.")
             return False
                        
