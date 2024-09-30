import random

emoji = {
    'r': 'R',
    'p': 'P',
    's': 'S'
}
choices = ('r', 'p', 's')

while True:
    user_input = input("Rock, paper, scissors? (r/p/s): ")

    if user_input not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emoji[user_input]}")
    print(f"Computer chose {emoji[computer_choice]}")

    if user_input == computer_choice:
        print("Tie!")

    elif ((user_input == 'r' and computer_choice == 's') or
          (user_input == 'p' and computer_choice == 'r') or
          (user_input == 's' and computer_choice == 'p')):
        print("You won")

    else:
        print("You lose")

        should_continue = input("You want to continue? (y/n): ")

        if should_continue == 'n':
            break
