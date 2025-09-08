import random
from enemy import Enemy

class Weeping_Angel(Enemy):

    def __init__(self, name):
        super().__init__(name)
        self.health = 400
        self.attack_power = 15

    def stealth(self):
        print("*All of the sudden you feel a stone statue standing behind you*")

    def take_damage(self, damage):
        print("You can't turn your back on a weeping angel..🤦‍♀️")
        return super().take_damage(damage)
    
    def trample(self):
        return 1000
    
    def is_alive(self):
        print("You decide to not blink...ever, smart.")
        return super().is_alive()

    def enrage_attack(self):
        choice = random.choice