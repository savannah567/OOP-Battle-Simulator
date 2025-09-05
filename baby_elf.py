from enemy import Enemy

class Baby_Elf(Enemy):
    def cry():
        print("wahhh :(")


    #Override Take Damage
    def take_damage(self,damage):
        print("Why would you hit this baby elf??? chill..")
        return super().take_damage(damage)