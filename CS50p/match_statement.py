name = input("What's your name? ").title()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Your House is Gryffindor")
    case "Draco":
        print("Your House is Slytherin")
    case _:
        print("You are not a student in Hogwarts")
