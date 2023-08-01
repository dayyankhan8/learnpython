import getpass
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
    ------------------------------|  How to Play?  |------------------------------
    {player1} will enter a word and {player2} will have to guess it in 6 attempts.
    Guessed letters will be shown after every attempt.
    If {player2} guesses the word in 6 attempts, {player1} loses.
    If {player2} is not able to guess the word in 6 attempts, {player1} wins.
    ---X---X------X-----X-----X-----X-----X-----X-----X-----X-----X-------X---X---
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