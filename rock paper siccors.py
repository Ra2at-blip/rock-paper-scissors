import random

choices = ("r", "p", "s")

while True:
    # ask user for decision
    user_choice = input("rock, paper or scissors? (r/p/s): ").lower()

    # if choice is not valid
    if user_choice not in choices:
        print("Invalid choice, try again.")
        continue

    # let computer make a choice
    computer_choice = random.choice(choices)

    # print choices
    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    # determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")
    ):
        print("You win!")
    else:
        print("You lose!")

    # ask if user wants to continue
    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == 'n':
        break
