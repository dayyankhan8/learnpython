import random

def print_intro():
    print("Welcome to the Dungeon Explorer!")
    print("You find yourself in a dark and creepy dungeon.")
    print("Your goal is to find the treasure and get out alive.")
    print("Beware of the monsters that lurk in the shadows!")
    print()

def get_player_choice():
    print("What would you like to do?")
    print("1. Explore the next room.")
    print("2. Fight the monster.")
    print("3. Flee the dungeon.")
    choice = input("Enter the number of your choice: ")
    return choice

def explore_room():
    print("You cautiously enter the next room.")
    if random.random() < 0.6:
        print("The room is empty. Safe for now!")
    else:
        print("A fearsome monster jumps out!")
        return True
    return False

def fight_monster():
    player_strength = 10
    monster_strength = random.randint(5, 15)
    print(f"A battle ensues with the monster (Monster Strength: {monster_strength}).")
    while player_strength > 0 and monster_strength > 0:
        player_attack = random.randint(1, 6)
        monster_attack = random.randint(1, 6)
        if player_attack > monster_attack:
            print("You hit the monster!")
            monster_strength -= player_attack
        else:
            print("The monster strikes back!")
            player_strength -= monster_attack
        print(f"Your Strength: {player_strength} | Monster Strength: {monster_strength}")
    return player_strength > 0

def main():
    print_intro()
    player_alive = True

    while True:
        choice = get_player_choice()

        if choice == '1':
            encounter_monster = explore_room()
            if encounter_monster:
                player_alive = fight_monster()
        elif choice == '2':
            if player_alive:
                player_alive = fight_monster()
            else:
                print("You cannot fight if you are already defeated!")
        elif choice == '3':
            print("You flee the dungeon. Better luck next time!")
            break
        else:
            print("Invalid choice. Try again!")

        if not player_alive:
            print("Game Over! You were defeated by the monster.")
            break

    if player_alive:
        print("Congratulations! You found the treasure and escaped the dungeon!")

if __name__ == "__main__":
    main()
