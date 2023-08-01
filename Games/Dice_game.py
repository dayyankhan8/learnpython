import random 


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