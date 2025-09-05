from enemy import Enemy

class Weeping_Angel(Enemy):

    def stealth():
        print("*All of the sudden you feel a stone statue standing behind you*")

    def take_damage(self, damage):
        print("You can't turn your back on a weeping angel..🤦‍♀️")
        return super().take_damage(damage)
    
    def is_alive(self):
        print("You decide to not blink...ever, smart.")
        return super().is_alive()

    def enrage_attack(self, damage):
        print("You hit the weeping angel! It gets enraged and attacks back!")
        return super().take_damage(damage // 2)