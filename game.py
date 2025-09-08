import random
from goblin import Goblin
from hero import Hero
from boss import Weeping_Angel

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Kevin Gates")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    rounds = 0
    total_damage = 0
    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds += 1
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        special_damage = hero.special_ability()
        print(f"Hero uses special ability on {target_goblin.name} for {special_damage} damage!")
        target_goblin.take_damage(special_damage)
        target_goblin.take_damage(damage)
        total_damage += damage
        
        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    print(f"Battle Summary:")

    print(f"Total number of rounds survived: {rounds}")
    print(f"Total Damage: {total_damage}")
    # Final tally of goblins defeated
    print(f"Total goblins defeated: {defeated_goblins} / {len(goblins)}")
    
    if hero.is_alive():
        print("BOSS BATTLE INCOMING")
        WeepingAngel = Weeping_Angel("Weeping Angel")
        while hero.is_alive() and WeepingAngel.is_alive():
            damage = hero.strike()
            WeepingAngel.take_damage(damage)
            stealth = WeepingAngel.stealth()
            print(f"Hero attacks Weeping Angel for {damage} damage!")
            damage = WeepingAngel.attack()
            hero.receive_damage(damage)
    if hero.is_alive():
        print("Hero has successfully deafeated the boss!")
    else:
        print("The hero has been defeated by the boss. Game Over. (｡•́︿•̀｡)")

if __name__ == "__main__":
    main()