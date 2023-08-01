import random

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

