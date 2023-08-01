import getpass
import random

def game1():

    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print("Try a higher number.")
        else:
            print("Try a lower number.")    

def game2():

        def roll_dice():
        return random.randint(1, 6)


    def player_turn(player, current_score):
        print(f"\n{player}'s turn.")
        input("Press Enter to roll the dice...")
        roll = roll_dice()

        if roll == 1:
            print(f"Oops! You rolled a 1. Your current score ({current_score}) is lost.")
            return 0
        else:
            print(f"Congratulations! You rolled a {roll}. Your current score is {current_score + roll}.")
            return current_score + roll


    def dice_game():
        player1_name = input("Enter the name of Player 1: ")
        player2_name = input("Enter the name of Player 2: ")

        player1_score = 0
        player2_score = 0

        while player1_score < 30 and player2_score < 30:
            player1_score = player_turn(player1_name, player1_score)
            print(f"{player1_name}'s total score: {player1_score}")

            if player1_score >= 30:
                break

            player2_score = player_turn(player2_name, player2_score)
            print(f"{player2_name}'s total score: {player2_score}")

        if player1_score >= 30:
            print(f"\nCongratulations! {player1_name} wins!")
        else:
            print(f"\nCongratulations! {player2_name} wins!")


    if __name__ == "__main__":
        dice_game()

def game3():

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

def game4():
     
        def get_riddle(level):
        # You can define your riddles for each level here.
        riddles = {
            1: "What is black when you purchase it, red while you are using it, and gray when you discard it?",
            2: "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
            3: "What has keys but can't open locks?",
            4: "The more you take, the more you leave behind. What am I?",
            5: "What comes once in a minute, twice in a moment, but never in a thousand years?",
            6: " I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
            7: " What has one head, one foot, and four legs?",
            8: "What gets wetter as it dries?",
            9: "What belongs to you but others use it more than you do?",
            10: "What has a neck but no head?",
            11: "I am full of holes but still holds water. What am I?",
            12: "What has a face but no eyes, hands but no arms?",
            13: "What can travel around the world while staying in a corner?",
            14: "What has to be broken before you can use it?",
            15: "What has a head, a tail, but no body?",
            16: "What comes down but never goes up?",
            17: "What can be cracked, made, told, and played?",
            18: "I have keys, but no locks. I have space, but no room. You can enter, but can't go outside. What am I?",
            19: "What has a thumb and four fingers but is not a hand?",
            20: "What is always in front of you but can't be seen?",


            # Add more riddles for levels 3 to 20...
        }

        return riddles.get(level, None)

    def get_answer(level):
        # You can define the correct answers for each level here.
        answers = {
            1: "coal",
            2: "echo",
            3: "piano",
            4: "footsteps",
            5: "m",
            6: "map",
            7: "bed",
            8: "towel",
            9: "name",
            10: "bottle",
            11: "sponge",
            12: "clock",
            13: "stamp",
            14: "egg",
            15: "coin",
            16: "rain",
            17: "joke",
            18: "keyboard",
            19: "glove",
            20: "future",

            # Add more answers for levels 3 to 20...
        }

        return answers.get(level, None)

    def riddle_game():
        print("Welcome to the Riddle Game!")
        print("You have 3 tries for each level.")
        score = 0

        for level in range(1, 21):
            riddle = get_riddle(level)
            answer = get_answer(level)
            if riddle is None or answer is None:
                print("Oops! Something went wrong. The game cannot continue.")
                return

            print(f"\nLevel {level}:")
            print(riddle)

            for tries in range(3):
                user_answer = input("\nEnter your answer: ").lower()
                if user_answer == answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    remaining_tries = 2 - tries
                    if remaining_tries > 0:
                        print(f"Incorrect! You have {remaining_tries} {'tries' if remaining_tries > 1 else 'try'} left.")
                    else:
                        print("Incorrect! You have used all your tries for this level.")
                        break

        print("\nGame Over!")
        print(f"Your final score is: {score} out of 20.")

    if __name__ == "__main__":
        riddle_game()

def game5():

    def display_hangman(tries):
        stages = [
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
            """,
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     /
            -
            """,
            """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |
            -
            """,
            """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |
            -
            """,
            """
            --------
            |      |
            |      O
            |      |
            |      |
            |
            -
            """,
            """
            --------
            |      |
            |      O
            |    
            |      
            |
            -
            """,
            """
            --------
            |      |
            |      
            |    
            |      
            |
            -
            """
        ]
        return stages[tries]

    def hangman():
        print("Welcome to Hangman!")
        player1 = input("Player 1, Please Enter your name: ").title().strip()
        player2 = input("player 2, Please enter your name: ").title().strip()
        print(f"""
    ------------------------------|  How to Play?  |-------------------------------
        {player1} will enter a word and {player2} will have to guess it in 6 attempts.
        Guessed letters will be shown after every attempt.
        If {player2} guesses the word in 6 attempts, {player1} loses.
        If {player2} is not able to guess the word in 6 attempts, {player1} wins.
    ----X---X------X-----X-----X-----X-----X-----X-----X-----X-----X-------X---X----
        """)
        word = getpass.getpass(f"{player1}, Please enter a word: ").lower()
        guessed_letters = set()
        incorrect_guesses = 0
        max_attempts = 6

        while True:
            display_word = ""
            for letter in word:
                if letter in guessed_letters:
                    display_word += letter
                else:
                    display_word += "_"

            print(display_hangman(incorrect_guesses))
            print("Guessed letters:", ", ".join(guessed_letters))
            print("Current word:", display_word)

            if display_word == word:
                print(f"Congratulations! {player2} guessed the word: {word} ")
                break

            if incorrect_guesses >= max_attempts:
                print(f"Sorry, {player2} lost! The word was: {word}")
                break

            guess = input(f"{player2}, enter a letter: ").lower()

            if guess in guessed_letters:
                print(f"{player2}, You have already guessed that letter!")
            else:
                guessed_letters.add(guess)
                if guess not in word:
                    incorrect_guesses += 1

    if __name__ == "__main__":
        hangman()


def main():
    print("\nWelcome!")
    print("""
          --| Game Selection Menu |--
          1. Guessing the Number Game
          2. Dice Rolling Game
          3. Treasure Hunt Game
          4. Riddles Game
          5. Hangman Game
          ----------------------------
          """
          )
    choice = input("Enter the Number of Game you want to play from  the selection menu above: ")

    if choice == 1:
        game1()
    elif choice == 2:
        game2()
    elif choice == 3:
        game3()
    elif choice == 4:
        game4()     
    elif choice == 5:
        game5()       
    else:
        print("Invalid choice. Exiting the program.")

if __name__ == "__main__":
    main()